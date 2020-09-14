import random
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
print('Code OS 1.0')
time.sleep(0.3)
print("Type 'cmdlist' for help")
while True:
    command = input('> ')
    if command == 'cmdlist':
        print('cmdlist-Show command list')
        time.sleep(0.05)
        print('newfile-Setup a new file')
        time.sleep(0.05)
        print('openfile-Open file')
        time.sleep(0.05)
        print('ver-Output version')
        time.sleep(0.05)
        print('time-Print datetime')
        time.sleep(0.05)
        print('shell-Show Python Shell')
        time.sleep(0.05)
        print('quit-Quit Code OS')
    elif command == 'newfile':
        fileName = input('newfile/fileName > ')
        if (fileName == ''):
            print("Error/name_error: name '' is not a char")
            continue
        else:
            print('newFile: Creating......')
            newFile = open(fileName, "w")
            fileContent = input('newfile/fileContent > ')
            newFile.write(fileContent)
            print('Done')
            newFile.close()
    elif command == 'openfile':
        try:
            fileName = input('openfile name > ')
            seeFile = open(fileName, "r")
            text = seeFile.readline()
            seeFile.close()
            print('seefile:', text)
        except:
            print((('Error/file_error: Cannot find ' + fileName) + '.'))
            continue
    elif command == 'ver':
        print("Code Oprating System ©2020 Allright reserved")
    elif command == 'quit':
        print('Closing...')
        break
    elif command == 'time':
        print(datetime.now())
    elif command == 'shell':
        print("Python shell")
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
                print(" Error python command")
    elif command == '':
        continue
    else:
        print("Error/command_error: Cannot find '", command, "'")