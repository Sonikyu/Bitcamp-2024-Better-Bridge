import socket
from _thread import *

host: str = '192.168.1.191'
port: int = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((host, port))
except socket.error as e:
    str(e)

numOfClients: int = 2

server.listen(numOfClients)
print("Waiting for a connection, server started")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print("Disconnected")
                break
            else:
                print(f"Recieved: {reply}")
                print(f"Sending: {reply}")
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection")
    conn.close()
while True:
    conn, addr = server.accept()
    print(f"Connected to: {addr}")

    start_new_thread(threaded_client, (conn, ))