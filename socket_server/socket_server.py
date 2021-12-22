import sys
import json
import socket


def receive_big_data(sock):
    buff_size = 1024
    data = b''
    while True:
        part = sock.recv(buff_size)
        data += part
        if len(part) < buff_size:
            # either 0 or end of data
            break
    return data


server_socket = socket.socket()

print("Server socket created")

ip = "127.0.0.1"

port = 35491

server_socket.bind((ip, port))

print("Server socket bound with with ip {} port {}".format(ip, port))

server_socket.listen()

count = 0

while True:
    try:
        client_connection, client_address = server_socket.accept()
        count += 1
        print(f"Accepted {count} {client_address} connections so far")
        while True:
            data = receive_big_data(client_connection)
            if data != b'':
                print(json.loads(data.decode()))
                msg1 = "Hi Client! Read everything you sent".encode()
                msg2 = "Now I will close your connection".encode()
                client_connection.send(msg1)
                client_connection.send(msg2)
                client_connection.close()
                print("Connection closed")
                break

    except KeyboardInterrupt:
        print('Server socket close')
        server_socket.close()
        sys.exit()
