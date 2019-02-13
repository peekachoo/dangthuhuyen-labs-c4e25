import mlab
from user import User

mlab.connect()

p = User(username="con10ngaynua", password="macungchuahocwritingnot")
p.save()

p_objects = User.objects()
p_first = p_objects[0]

p = p_objects[0]
p.update(set__username="khongphaihuyen", set__password="passvanthe")
p.reload()