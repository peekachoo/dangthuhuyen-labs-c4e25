import mlab
from food import Food

mlab.connect()

# 1. Create:
# 1.1. Create a food:
f = Food(title="Banh canh", link="https://static1.squarespace.com/static/52d3fafee4b03c7eaedee15f/t/5a0a08cbec212d1131d5d33d/1510607073306/banh-canh-2.jpg")
# 1.2. Save it:
# f.save()

# 2. Read:
# 2.1. Get cursor:
f_objects = Food.objects() # Lazy loading # Consider as a list
# 2.2. Process cursor:
# f_first = f_objects[0] # Actual data transfering
# print(f_first, f_first.title, f_first.link)

# print(len(f_objects)) # Slow
# print(f_objects.count())

# for f in f_objects:
#     print(f.title)
#     print(f.link)
#     print("------------------")

# 3. Update:
# f = f_objects[0] # Update theo vi tri
# f.update(set__title="Banh rat ngon", set__link="Link ngon")
# f.reload()
# print(f.title)


# 4. Delete:
# f.delete()

# Xoa bang id:
f = f_objects.with_id("5c4d7dcc2e1aaf14246e575d") # 0
if f != None: # TH id sai
    f.delete()
    print("Deleted.")
else:
    print("Not found.")