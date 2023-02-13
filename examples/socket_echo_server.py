import time
import socket 

from cc.serializer import SocketSerializer

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", 50001))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)

        ser = SocketSerializer(conn)
        ser.setReceiveTimeout(0.1)
        
        while True:
            buffer = ser.receive()
            print("recv:", buffer)
            ser.transmit(buffer)
