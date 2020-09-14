from cefpython3 import cefpython as cef
import platform
import sys

def main():
    try:
        file = open("homePage.set","r")
        home = file.readline()
    except:
        file = open("homePage.set","w")
        home = input("setup_homepage >")
        file.write(home)
        file.close()
    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    cef.CreateBrowserSync(url= input("url >"),window_title="Aser Conet")
    cef.MessageLoop()
    cef.Shutdown()

if __name__ == '__main__':
    main()
