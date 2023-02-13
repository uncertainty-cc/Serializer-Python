import time
import socket

from cc.serializer import SocketSerializer

def connect():
    s = None
    while not s:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("127.0.0.1", 50001))
        except ConnectionRefusedError:
            s = None
            continue
    ser = SocketSerializer(s)
    return s, ser


s, ser = connect()
ser.transmit(b'Hello, world')

ser.setReceiveTimeout(0.1)

while True:
    pass
    try:
        buffer = ser.receive()
    except (ConnectionAbortedError, ConnectionResetError):
        s, ser = connect()
        ser.transmit(b'Hello, world1')

    print("recv:", buffer)
    try:
        ser.transmit(buffer)
    except (ConnectionAbortedError, ConnectionResetError):
        s, ser = connect()
        ser.transmit(b'Hello, world2')

