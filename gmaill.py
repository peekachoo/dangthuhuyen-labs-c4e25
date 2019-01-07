sicknesses = ["máu trắng", "ung thư", "xương thuỷ tinh"]

from gmail import GMail, Message
import random
# hoặc dùng from random import choice
# sickness = choice(sicknesses)

t = '''
<p><strong>Ch&agrave;o sếp,</strong></p>
<p>H&ocirc;m nay em bị <strong>{{sickness}}</strong></p>
<p>Sếp cho em xin <em>nghỉ l&agrave;m h&ocirc;m nay.</em></p>
<p>&nbsp;</p>
'''

sickness = random.choice(sicknesses)
t_content = t.replace("{{sickness}}", sickness)
# t_content = t.replace("{{sickness}}", sickness).replace("", ) -> replace thêm

gmail = GMail('Peekachoo <limerence.al@gmail.com','thu12345')
msg = Message('Test Message',to='Huy <qhuydtvd@gmail.com',html=t_content)
gmail.send(msg)

print(t_content)