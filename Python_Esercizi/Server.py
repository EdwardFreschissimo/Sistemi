import socket
import turtle

passo=50
angolo=90

host = '127.0.0.1'
port = 65432
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen()
conn, addr = s.accept()
t=turtle.Turtle()
while True: 
    data= conn.recv(4096)
    print(data.decode())
    k=data.decode()
    for k in data.decode():
        if(k=='f'):
            t.forward(passo)
            x, y=t.pos
            conn.sendall(("COORD: " + str(x).encode()+", "+ str(y)).encode())
        elif(k=='l'):
            t.left(angolo)
            x, y=t.pos()
            conn.sendall(("COORD: " + str(x).encode()+", "+ str(y)).encode())
        elif(k=='r'):
            t.right(angolo)
            x, y=t.pos()
            conn.sendall(("COORD: " + str(x).encode()+", "+ str(y)).encode())
        elif(k=='b'):
            t.back(passo)
            x, y=t.pos()
            conn.sendall(("COORD: " + str(x).encode()+", "+ str(y)).encode())

    conn.sendall(data)



