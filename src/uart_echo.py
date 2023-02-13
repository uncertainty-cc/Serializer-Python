import time
import socket 

from cc.serializer import SocketSerializer


def waitForConnection(sock):
    conn = None
    while not conn:
        try:
            conn, addr = s.accept()
        except TimeoutError:
            continue
    ser = SocketSerializer(conn)
    ser.setReceiveTimeout(0.1)
    print("Connected by", addr)
    return conn, addr, ser

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", 50001))
    s.listen(1)
    s.settimeout(1)

    conn, addr, ser = waitForConnection(s)    
    while True:
        try:
            buffer = ser.receive()
        except (ConnectionAbortedError, ConnectionResetError):
            print("disconnected.")
            print("reconnecting...")
            conn, addr, ser = waitForConnection(s)
            continue
        print("recv:", buffer)
        try:
            ser.transmit(buffer)
        except (ConnectionAbortedError, ConnectionResetError):
            print("disconnected.")
            print("reconnecting...")
            conn, addr, ser = waitForConnection(s)
            continue

