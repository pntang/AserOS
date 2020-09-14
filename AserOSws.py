import random
import sys
import time
import datetime
from datetime import datetime

print("Starting BIOS...")
time.sleep(1)
print("Starting System...")
time.sleep(1)
print(" ")
print('Aser Oprating System - WorkStation ©2020 All right reserved')
time.sleep(0.3)
print("Type 'cmdlist' for help")
while True:
    command = input('>>>')
    if command == 'cmdlist':
        print('Aser/commandlist > cmdlist')
        time.sleep(0.05)
        print('Aser/commandlist > newfile')
        time.sleep(0.05)
        print('Aser/commandlist > openfile')
        time.sleep(0.05)
        print('Aser/commandlist > seefile')
        time.sleep(0.05)
        print('Aser/commandlist > quit')
        time.sleep(0.05)
        print('Aser/commandlist > ver')
        time.sleep(0.05)
        print('Aser/commandlist > time')
        time.sleep(0.05)
        print('Disk Drive > disk')
    elif command == 'newfile':
        fileName = input('filename >>>')
        if (fileName == ''):
            print("Error")
            continue
        else:
            print('Creating...')
            newFile = open(fileName, "w")
            fileContent = input('filecontent >>>')
            newFile.write(fileContent)
            print('Done')
            newFile.close()
    elif command == 'openfile':
        try:
            fileName = input('fileName >>>')
            alterType = input('alterType >>>')
            alterFile = open(fileName, alterType)
            fileContent = input('fileContent >>>')
            print('alter......')
            alterFile.write(fileContent)
            print('Done')
            alterFile.close()
        except:
            print('Error')
            continue
    elif command == 'seefile':
        try:
            fileName = input('filename >>>')
            seeFile = open(fileName, "r")
            text = seeFile.readline()
            seeFile.close()
            print('seefile:', text)
        except:
            print('Error')
            continue
    elif command == 'ver':
        print("&&&&&  Aser Oprating System - WorkStation")
        time.sleep(0.05)
        print("&   &  Aser inc. ©2020 All right reserved")
        time.sleep(0.05)
        print("&&&&&  Version:12.21 - WorkStation")
        time.sleep(0.05)
        print("&   &  Environment:Python3.8.5")
        time.sleep(0.05)
        print("&   &  Num:2008-2012-04-1221")
    elif command == 'quit':
        print('Closing...')
        time.sleep(0.5)
        break
    elif command == 'time':
        print(datetime.now())

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
            elif Disk == "runc":
                print(" Running DiskC...")
                time.sleep(1)
                import DiskC
                print(" Done")
            elif Disk == "rund":
                print(" Running DiskD...")
                time.sleep(1)
                import DiskD
                print(" Done")
            elif Disk == "rune":
                print(" Running DiskE...")
                time.sleep(1)
                import DiskE
                print(" Done")
            elif Disk == "runf":
                print(" Running DiskF...")
                time.sleep(1)
                import DiskF
                print(" Done")
            elif Disk == "rung":
                print(" Running DiskG...")
                time.sleep(1)
                import DiskG
                print(" Done")
            elif Disk == "quit":
                break
            else:
                print(" Running Failed")
    elif command == 'ws':
        import AserOSws
    elif command == 'regedit':
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
    else:
        print("Error")
