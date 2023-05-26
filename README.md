# Lectura de Valores Analógicos del Sensor EMG

Este repositorio contiene el código necesario para realizar la lectura de valores analógicos del sensor EMG usando un arduino UNO y enviarlos a Python a través del puerto serial. Los valores leídos se guardarán en un archivo CSV, con un límite máximo de 500 valores.

## Requisitos

- Arduino IDE
- Placa Arduino compatible
- Sensor EMG conectado a la placa Arduino
- Python 3.x instalado en tu sistema

## Instrucciones de Uso

1. Conecta el sensor EMG a la placa Arduino según las especificaciones del hardware.
2. Abre el archivo `arduino_code.ino` en Arduino IDE.
3. Selecciona el tipo de placa y el puerto correcto en Arduino IDE.
4. Sube el código a la placa Arduino.
5. Abre el archivo `python_code.py` en un editor de texto o entorno de desarrollo Python.
6. Asegúrate de tener instalada la biblioteca `pyserial` ejecutando el siguiente comando:
   ```
   pip install pyserial
   ```
7. Modifica el puerto serial en el código Python si es necesario.
8. Ejecuta el código Python.
9. Se recopilarán y guardarán automáticamente los 500 valores leídos del sensor EMG en un archivo CSV llamado `data.csv`.

## Comunicación entre Arduino y Python

Para establecer la comunicación entre Arduino y Python a través del puerto serial, se ha utilizado el enfoque descrito en el siguiente post del foro de Arduino:

- [Serial Input Basics (Updated)](https://forum.arduino.cc/t/serial-input-basics-updated/382007/3)

El código en Arduino se basa en los principios presentados en ese post para recibir y procesar los datos enviados desde Python.

## Próximas Mejoras
Para una próxima versión de este proyecto, se tiene planeado implementar el filtro de Kalman para mejorar la precisión y estabilidad de los valores leídos del sensor EMG. Esto permitirá obtener resultados más suaves y filtrados.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si encuentras algún error, tienes ideas de mejora o deseas añadir nuevas funcionalidades, no dudes en enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más información.

¡Esperamos que este código te sea útil! Si tienes alguna pregunta o consulta, no dudes en contactarnos.
