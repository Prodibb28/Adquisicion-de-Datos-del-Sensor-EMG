import serial
import time
import csv

startMarker = '<'
endMarker = '>'
dataStarted = False
dataSave = False
dataBuf = ""
messageComplete = False
reads = []


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
          print(msg)
            

            



#====================
#====================
    # the program

setupSerial(115200, "COM11")
count = 0
prevTime = time.time()
dataSave = False
while count!=500:
    arduinoReply = recvLikeArduino()
    if not (arduinoReply == 'XXX' ) :
        reads.append(arduinoReply)
        print(count)
        count += 1
with open("measures.csv", "a+", newline ='') as csvfile:
        wr = csv.writer(csvfile, dialect='excel', delimiter=',')
        for x in reads:
            wr.writerow([x])
  

  

    
#totalMavIa = [36,25,3,4]

# with open('Phj.txt', 'a', newline='') as csvfile:
#     csvfile.write(','.join(totalMavIa))
#     csvfile.write(',')
   

 