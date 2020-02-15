import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    IP_SERVER = input("IP server: ")
    pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    test = pat.match(IP_SERVER)
    if test:
        while True:
            PORT = input("PORT server: ")
            pat = re.compile("^()([1-9]|[1-5]?[0-9]{2,4}|6[1-4][0-9]{3}|65[1-4][0-9]{2}|655[1-2][0-9]|6553[1-5])$")
            test = pat.match(PORT)
            PORT = int(PORT)
            if test:
                break
            else:
                print("\nPORTA NON CORRETTA\n")
        break
    else:
        print("\nIP NON CORRETTO\n")
    


s.connect((IP_SERVER, PORT))
while True:
    try:
        text = input("Messaggio: ")
    except KeyboardInterrupt:
        s.sendall("EXIT".encode())
        break
    

    if text == "EXIT":
        s.sendall(text.encode())
        break
        
    else:
        if text != "":
            s.sendall(text.encode())
            data = s.recv(4096)
            print("Server: " + data.decode())

s.close()