import serial
import time
import csv

startMarker = '<'
endMarker = '>'
dataStarted = False
dataBuf = ""
messageComplete = False
measures = []


def setupSerial(baudRate, serialPortName):
    
    global  serialPort
    
    serialPort = serial.Serial(port= serialPortName, baudrate = baudRate, timeout=0, rtscts=True)

    print("Serial port " + serialPortName + " opened  Baudrate " + str(baudRate))

    waitForArduino()

#========================

def sendToArduino(stringToSend):
    
        # this adds the start- and end-markers before sending
    global startMarker, endMarker, serialPort
    
    stringWithMarkers = (startMarker)
    stringWithMarkers += stringToSend
    stringWithMarkers += (endMarker)

    serialPort.write(stringWithMarkers.encode('utf-8')) # encode needed for Python3


#==================

def recvLikeArduino():

    global startMarker, endMarker, serialPort, dataStarted, dataBuf, messageComplete

    if serialPort.inWaiting() > 0 and messageComplete == False:
        x = serialPort.read().decode('utf-8') # decode needed for Python3
        
        if dataStarted == True:
            if x != endMarker:
                dataBuf = dataBuf + x
            else:
                dataStarted = False
                messageComplete = True
        elif x == startMarker: 
            dataBuf = ''
            dataStarted = True
    
    if (messageComplete == True):
        messageComplete = False
        return dataBuf
    else:
        return "XXX" 

#==================

def waitForArduino():

    # wait until the Arduino sends 'Arduino is ready' - allows time for Arduino reset
    # it also ensures that any bytes left over from a previous message are discarded
    
    print("Waiting for Arduino to reset")
     
    msg = ""
    while msg.find("Arduino is ready") == -1:
        msg = recvLikeArduino()
        if not (msg == 'XXX'): 
          sendToArduino("StartMeasure")
          measures.append("v#i#t")
          print(msg)
            

            



#====================
#====================
    # the program

setupSerial(115200, "COM14")
count = 0
prevTime = time.time()
while True:
            # check for a reply
    
    arduinoReply = recvLikeArduino()
    if not (arduinoReply == 'XXX' or arduinoReply == 'Finish' ):
        measures.append(arduinoReply)
    if (arduinoReply == 'Finish' and count==0):
        with open("miguel.csv", "a+", newline ='') as csvfile:
         wr = csv.writer(csvfile, dialect='excel', delimiter=',')
         print("entro")
         for x in measures:
          wr.writerow([x])
        
    
#totalMavIa = [36,25,3,4]

# with open('Phj.txt', 'a', newline='') as csvfile:
#     csvfile.write(','.join(totalMavIa))
#     csvfile.write(',')
   

 