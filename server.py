from scheduler import Scheduler
import socket
import system_call
import time

def handler(conn,addr):
    try:
        while True:
            yield system_call.WaitRead(conn)
            data = conn.recv(200).decode()
            print('the %s sends a message: %s' %(addr, data))
            conn.sendall('hello'.encode())
    except Exception:
        conn.close()
        print('%s quit'%addr[0])

def server():
    print('Your web server are opening')
    s = socket.socket()
    s.bind(('192.168.199.147', 8888))
    s.listen(5)
    while True:
        yield system_call.WaitRead(s)
        conn, addr = s.accept()
        yield system_call.NewTask(handler(conn,addr))


print("Starting BIOS...")
time.sleep(1)
print("Starting System...")
time.sleep(1)
print(' ')
print("Aser Oprating System - Server_run ©2020 All right reserved")
time.sleep(0.3)
print("Type server to run web server")
while True:
    cmd = input("> ")
    if cmd == 'server':
        s = Scheduler()
        # s.new(alive())
        s.new(server())
        s.main_loop()
    elif cmd == 'quit':
        break
    elif cmd == 'ver':
        print("&&&&&  Aser Oprating System - Server_run")
        time.sleep(0.05)
        print("&   &  Aser inc. ©2020 All right reserved")
        time.sleep(0.05)
        print("&&&&&  Version:12.4 - Server_run")
        time.sleep(0.05)
        print("&   &  Environment:Python3.8.5")
        time.sleep(0.05)
        print("&   &  Num:2008-2012-04-1224.2")