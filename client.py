import socket
import time

def client():
    s = socket.socket()
    s.connect(('192.168.199.147', 8888))
    try:
        while True:
            input_data = input(' Message > ').encode()
            s.sendall(input_data)
            print(s.recv(200).decode())
    except:
        s.close()

print("Starting BIOS...")
time.sleep(1)
print("Starting System...")
time.sleep(1)
print(' ')
print("Aser Oprating System - Server_Contect ©2020 All right reserved")
time.sleep(0.3)
print("Type server to contect web server")
while True:
    cmd = input("> ")
    if cmd == 'server':
        client()
    elif cmd == 'quit':
        break
    elif cmd == 'ver':
        print("&&&&&  Aser Oprating System - Server_contect")
        time.sleep(0.05)
        print("&   &  Aser inc. ©2020 All right reserved")
        time.sleep(0.05)
        print("&&&&&  Version:12.4 - Server_contect")
        time.sleep(0.05)
        print("&   &  Environment:Python3.8.5")
        time.sleep(0.05)
        print("&   &  Num:2008-2012-04-1224.1")
def client():
    s = socket.socket()
    s.connect(('192.168.199.147', 8888))
    try:
        while True:
            input_data = input(' Message > ').encode()
            s.sendall(input_data)
            print(s.recv(200).decode())
    except:
        s.close()



