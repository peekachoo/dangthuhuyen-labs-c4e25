# Exercise1:
def greet():
    print("Hello world")
    print("Hello world")
    print("Hello world")


# Exercise2:
def sum(t, h):
    s = t + h
    print(s)


# Exercise3-4:
from turtle import *

def draw_square(length, color):
    pencolor(color)
    for i in range(4):
        forward(length)
        left(90)

speed(0)
for i in range(30):
    draw_square(i * 5, "red")
    left(17)
    penup()
    forward(i * 2)
    pendown()


# Exercise5-6:
def draw_star(x, y, length):
    penup()
    setpos(x,y)
    pendown()
    left(36)
    for i in range(5):
        forward(length)
        left(144)

speed(0)
color("blue")
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star (x, y, length)

mainloop()