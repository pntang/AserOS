import sys
import time
import os
import datetime
from datetime import datetime

print("Starting BIOS...")
time.sleep(1)
print("Starting System...")
time.sleep(1)
print(" ")
Login = input("Login > ")
print(" ")
print('Aser Oprating System - Siena ©2020 All right reserved')
time.sleep(0.3)
print("Type 'cmdlist' for help")
while True:
    command = input('> ')
    if command == 'cmdlist':
        print('Aser/commandlist > cmdlist\Show command list')
        time.sleep(0.05)
        print('Aser/commandlist > newfile\Setup a new file.')
        time.sleep(0.05)
        print('Aser/commandlist > openfile\Alter files')
        time.sleep(0.05)
        print('Aser/commandlist > seefile\See a file')
        time.sleep(0.05)
        print('Aser/commandlist > quit\Quit ')
        time.sleep(0.05)
        print('Aser/commandlist > ver\Output version.')
        time.sleep(0.05)
        print('Aser/commandlist > time\Print datetime')
        time.sleep(0.05)
        print('Aser/commandlist > applist\Show all apps')
    elif command == 'newfile':
        fileName = input('newfile/filename > ')
        if (fileName == ''):
            print("Error/name_error: name '' is not a char")
            continue
        else:
            print('newfile: Creating......')
            newFile = open(fileName, "w")
            fileContent = input('newfile/filecontent > ')
            newFile.write(fileContent)
            print('Done')
            newFile.close()
    elif command == 'openfile':
        try:
            fileName = input('openfile/filename > ')
            alterType = input('openfile/alterType -Write_or_Add > ')
            alterFile = open(fileName, alterType)
            fileContent = input('openfile/alter/filecontent > ')
            print('alter......')
            alterFile.write(fileContent)
            print('Done')
            alterFile.close()
        except:
            print((('Error/file_error: Cannot find ' + fileName) + '.'))
            continue
    elif command == 'seefile':
        try:
            fileName = input('seefile/filename > ')
            seeFile = open(fileName, "r")
            text = seeFile.readline()
            seeFile.close()
            print('seefile:', text)
        except:
            print((('Error/file_error: Cannot find ' + fileName) + '.'))
            continue
    elif command == 'ver':
        print("&&&&&  Aser Oprating System - Siena")
        time.sleep(0.05)
        print("&   &  Aser inc. ©2020 All right reserved")
        time.sleep(0.05)
        print("&&&&&  AseX kernel Copyright ©2020")
        time.sleep(0.05)
        print("&   &  Aser OS Version:15.0 - Siena")
        time.sleep(0.05)
        print("&   &  Aser OS Login:",Login)
    elif command == 'quit':
        print('Closing...')
        time.sleep(0.5)
        break
    elif command == 'time':
        print(datetime.now())
    elif command == 'applist':
        print("Applist")
        time.sleep(0.05)
        print("Aser Vitual System<aservs>")
        time.sleep(0.05)
        print("Python Shell<shell>")
        time.sleep(0.05)
        print("Chatbot<chatbot>")
        time.sleep(0.05)
        print("Disk Drive<disk>")
        time.sleep(0.05)
        print("WorkStation<ws>")
        time.sleep(0.05)
        print("Notepad<notepad>")
        time.sleep(0.05)
        print("Server<server>")
        time.sleep(0.05)
        print("Contect<contect>")
        time.sleep(0.05)
        print("Net<net>")
        time.sleep(0.05)
        print("CodeOS<codeos>")
    elif command == "aservs":
        print(" >Aser Vitual System <Aser.inc ©2020 All right reserved>")
        time.sleep(1)
        while True:
            vs = input(" >")
            if vs == "ZoreOS":
                print(" ")
                print(" Starting Vitual Machine...")
                time.sleep(1)
                print(" Installing BIOS...")
                time.sleep(1)
                print(" Installing System...")
                time.sleep(3)
                print(" ")
                print(" Zore OS 5.0")
                time.sleep(0.05)
                print(" Type list for command list")
                while True:
                    cmd = input(" > ")
                    if cmd == 'list':
                        print(" list > list/output command list")
                        time.sleep(0.05)
                        print(" list > ver/check Zore OS version")
                        time.sleep(0.05)
                        print(" list > new/create a new file")
                        time.sleep(0.05)
                        print(" list > open/open a file")
                        time.sleep(0.05)
                        print(" list > time/check datetime")
                        time.sleep(0.05)
                        print(" list > logout/close Zore OS")
                    elif cmd == 'ver':
                        print(" ver > Zore Oprating System ©2020 All right reserved")
                        time.sleep(0.05)
                        print(" Copyright > Aser Technology.inc")
                        time.sleep(0.05)
                        print(" num > 2080-5084-70-021")
                    elif cmd == 'new':
                        fname = input(' Filename >')
                        if (fname == ''):
                            print(" error > Filename cannot be empty")
                            continue
                        else:
                            print(' >creating... ')
                            newf = open(fname, "w")
                            fc = input(' write >')
                            newf.write(fc)
                            print(' Done')
                            newf.close()
                    elif cmd == 'open':
                        try:
                            fname = input(' FileName >')
                            seef = open(fname, "r")
                            txt = seef.readline()
                            seef.close()
                            print(' File/', txt)
                        except:
                            print(' error > Cannot find the file')
                            continue
                    elif cmd == 'time':
                        print(' ',datetime.now())
                    elif cmd == 'logout':
                        print(" Closing...")
                        time.sleep(3)
                        break
                    elif cmd == '':
                        continue
                    else:
                        print(" error > Cannot find '",cmd,"'")
            elif vs == "loados":
                loados = input(" LoadOS Disk>")
                os.system(loados)
            elif vs == "quit":
                break
            elif vs == "help":
                print(" HelpList")
                time.sleep(0.05)
                print(" |ZoreOS > Run ZoreOS locally")
                time.sleep(0.05)
                print(" |loados > Load OS Disk")
                time.sleep(0.05)
                print(" |quit > Quit Vitual System")
            elif vs == "":
                continue
            else:
                print(" Error Vitual System command")
    elif command == 'shell' and Login == 'Admin':
        print(" </> python shell build 3.8.5")
        while True:
            shell = input(" $ ")
            if shell == 'platform':
                print(" ",sys.platform)
            elif shell == 'version':
                print(" ",sys.version)
            elif shell == 'copyright':
                print(" ",sys.copyright)
            elif shell == 'time':
                print(" ",datetime.now())
            elif shell == 'run':
                srun = input(" $ run ")
                os.system(srun)
            elif shell == 'cmd':
                os.system(shell)
            elif shell == 'quit':
                break
            elif shell == '':
                continue
            else:
                print(" error python command")
    elif command == '':
        continue
    elif command == 'chatbot':
        print(' Chatbot build 1.0')
        time.sleep(0.1)
        chatname = input (' Enter your nickname:')
        time.sleep(0.1)
        print(' Type to chat')
        while True:
            chat = input(" "+chatname+" >")
            if 'hi' in chat:
                print(" Sprinkle > Hi~")
            elif 'hello' in chat:
                print(" Sprinkle > Hello~")
            elif 'your name' in chat:
                print(" Sprinkle > My name is Sprinkle~")
            elif 'how old' in chat:
                print(" Sprinkle > I'm fifteen years old.")
            elif 'age' in chat:
                print(" Sprinkle > I'm fifteen.")
            elif 'joke' in chat:
                print(" Sprinkle > Haha?")
            elif '( ﾟ∀。)' in chat:
                print(" Sprinkle > ( ﾟ∀。)")
            elif 'bye' in chat:
                print(" Sprinkle > Byebye~")
                break
            elif '' in chat:
                print(" Sprinkle > ???")
            else:
                print(" Sprinkle > Ha???")
        continue
    elif command == 'disk':
        print(" Disk Drive ©2020 Allright reserved")
        while True:
            Disk = input(" Disk/ >")
            if Disk == "run":
                print(" Running Disk...")
                time.sleep(1)
                import Disk
                print(" Done")
            elif Disk == "runa":
                print(" Running DiskA...")
                time.sleep(1)
                import DiskA
                print(" Done")
            elif Disk == "runb":
                print(" Running DiskB...")
                time.sleep(1)
                import DiskB
                print(" Done")
            elif Disk == "quit":
                break
            else:
                print(" Running Failed")
    elif command == 'ws':
        import AserOSws
    elif command == 'contect':
        import client
    elif command == 'server':
        import server
    elif command == 'net':
        import net
    elif command == 'codeos':
        import CodeOS
    elif command == 'notepad':
        while True:
            np = input(" >")
            if np == "new":
                l1 = input(" |")
                l2 = input(" |")
                l3 = input(" |")
                l4 = input(" |")
                l5 = input(" |")
            elif np == "open":
                print(l1)
                time.sleep(0.05)
                print(l2)
                time.sleep(0.05)
                print(l3)
                time.sleep(0.05)
                print(l4)
                time.sleep(0.05)
                print(l5)
            elif np == "quit":
                break
            else:
                print(" Error Note command")
    elif command == 'regedit' and Login == 'Admin':
        print("Regedit List")
        time.sleep(0.05)
        print("|   AppList    |   Cmd    |   Num   |")
        time.sleep(0.05)
        print("|   Newfile    | newfile  | 1201001 |")
        time.sleep(0.05)
        print("|   Seefile    | seefile  | 1201002 |")
        time.sleep(0.05)
        print("|   Openfile   | openfile | 1202003 |")
        time.sleep(0.05)
        print("|   Aser Vs    |  aservs  | 1202004 |")
        time.sleep(0.05)
        print("|   Chatbot    | chatbot  | 1202005 |")
        time.sleep(0.05)
        print("| Python Shell |  shell   | 1202006 |")
        time.sleep(0.05)
        print("|  Disk Drive  |   disk   | 1202007 |")
        time.sleep(0.05)
        print("|  WorkStation |    ws    | 1202008 |")
        time.sleep(0.05)
        print("|   Notepad    |  notepad | 1202009 |")
        time.sleep(0.05)
        print("|    Server    |  server  | 1202010 |")
        time.sleep(0.05)
        print("|   Contect    |  contect | 1202011 |")
        time.sleep(0.05)
        print("|     net      |    net   | 1202012 |")
        time.sleep(0.05)
        print("|    codeos    |  codeos  | 1202013 |")
    elif command == '_login_' and Login == '010100110111100101110011011101000110010101101101':
        print("Login : System")
    else:
        print("Error/command_error: Cannot find '", command, "'")
