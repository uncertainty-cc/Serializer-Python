import time
import socket

from cc.serializer import SocketSerializer

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 50001))

    ser = SocketSerializer(s)

    ser.transmit(b'Hello, world')
    
    ser.setReceiveTimeout(0.1)

    counter = 0
    while True:
        buffer = ser.receive()
        print("recv:", buffer)
        ser.transmit("{}".format(counter).encode())
        counter += 1

