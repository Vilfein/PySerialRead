import serial
import time

SerialObj = serial.Serial('COM4')  # COMxx   format on Windows
# ttyUSBx format on Linux

SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8  # Number of data bits = 8
SerialObj.parity = 'N'  # No parity
SerialObj.stopbits = 1  # Number of Stop bits = 1

SerialObj.timeout = None  # Setting timeouts here No timeouts,waits forever

#time.sleep(3)  # needed only for arduino
while 1:
    ReceivedString = SerialObj.readline()
    data = ReceivedString.decode('utf-8')
    print(data.rstrip('\n'))
    if '5' in data:
        break


SerialObj.close()