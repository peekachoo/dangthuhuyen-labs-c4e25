import datetime

run_once = 0

from gmail import GMail, Message

while run_once == 0:
    now = datetime.datetime.now()
    if now.hour == 7 :
        gmail = GMail('Peekachoo <limerence.al@gmail.com','thu12345')
        msg = Message('Test Message',to='Huy <qhuydtvd@gmail.com',text='My call-in-sick.')
        gmail.send(msg)
        run_once += 1
