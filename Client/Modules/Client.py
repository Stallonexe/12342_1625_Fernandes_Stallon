import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.137.1"

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def Send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

Send("Create RegUser stallonfernandes11@gmail.com ABCDEF Password FirstName Surname 07440423797")
Send("Retrieve Salt stallonfernandes11@gmail.com")
Send("Verify Email stallonfernandes11@gmail.com")
Send("Verify Password stallonfernandes11@gmail.com  Password")
Send("Verify Email stallonfernandes11@gmail.com")



#Send("!Register stallonfernandes11@gmail.com 162558 Password123 Stallon Fernandes 0123456789")
#Send("!Verify Email stallonfernandes11@gmail.com")
#input()
#Send("!Verify Hash stallonfernandes11@gmail.com Password123")
#input()
#Send("!Get Salt stallonfernandes11@gmail.com")
#input()
#Send("!Verify Email stallonfernandes11@gmail.com")
#input()
#Send("!Send OTP stallonfernandes11@gmail.com Stallon")
#input()
#Send("!Send BookingConfrimation ferns311@stgregorys.school Stallon St Gregorys Estate Denzil 11/05/2024 15:00 3 Potters Road Southall UB2 4AS")
#input()
