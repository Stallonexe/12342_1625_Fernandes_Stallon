import socket
import threading
from Commands import *
from datetime import datetime
import json


# Constants
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def CurrentTime():
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    return timestamp


def log(console_command):
    with open("logs.txt","a") as log:
        log.writelines(f"{console_command}\n")
        log.close()
        print(console_command)

def ServerClient(conn, addr):
    display_text = f"\n[NEW CONNECTION {CurrentTime()}] {addr} connected."
    log(display_text)

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            display_text = f"[{CurrentTime()}][{addr}] {msg}"
            log(display_text)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                display_text = f"[{CurrentTime()}][{addr}] DISCONNECTED"
                log(display_text)

            else:
                decoder = Command()
                reply = decoder.execute(message=msg)

                print(reply)
                if type(reply) == dict:
                    PropertyJson = json.dumps(reply, ensure_ascii=False)
                    conn.send("PropertyJson".encode(FORMAT))
                    conn.send(PropertyJson.encode(FORMAT))

                if reply is not None and len(reply) != 0:
                    conn.send(reply.encode(FORMAT))
                    log(f"[{CurrentTime()}][SERVER] {reply}")
                else:
                    conn.send("Done".encode(FORMAT))
                    log(f"[{CurrentTime()}][SERVER] {reply}")

    conn.close()

def start():
    server.listen()

    display_txt = f"\n[{CurrentTime()}] Server is online\n[LISTENING] Server is listening on {SERVER}"
    log(display_txt)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=ServerClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")

start()
