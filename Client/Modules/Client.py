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

    reply = client.recv(2048).decode(FORMAT)

    print(reply)

#Send("Create RegUser stallonfernandes11@gmail.com ABCDEF Password FirstName Surname 07440423797")
Send("Retrieve Salt stallonfernandes11@gmail.com") #reply
Send("Verify Email stallonfernandes11@gmail.com")
Send("Verify Password stallonfernandes11@gmail.com  Password")

Send("Create RegProperty H10 350000 77CoplandRoad HA04YF 1 1 1 leasehold C FLAT B")
Send("Create RegProperty H1 450000 3PottersRoad UB24AS 2 2 1 freehold C TERRACED B")
Send("Create RegProperty H2 5000000 123dhs SN1020 1 1 1 leasehold C FLAT B")
Send("Send PropertyJSON U10 400000 100000 HA 1 1 1 leasehold FLAT")
#Send("Verify Email stallonfernandes11@gmail.com")
#Send()



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
