import time

from cc.serializer import UARTSerializer

ser = UARTSerializer(port="COM1", baudrate=115200)

# wait for Arduino to reset Serial port
time.sleep(2)

ser.transmit(b"hello")

ser.setReceiveTimeout(0.1)

while True:
    buffer = ser.receive()
    print("recv:", buffer)
    ser.transmit(buffer)
