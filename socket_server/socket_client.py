import json
import socket


def send(data):
    socket_object = socket.socket()
    socket_object.connect(("localhost", 35491))

    print("Connected to localhost")
    msg = json.dumps(data)
    socket_object.sendall(msg.encode())

    while True:
        data = socket_object.recv(1024)
        print(data.decode())
        if data == b'':
            print("Connection closed")
            break
    socket_object.close()


big_data = list(range(100000))

while big_data:
    send(big_data[:1000])
    big_data = big_data[1000:]