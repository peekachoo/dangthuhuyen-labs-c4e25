from random import *
import sys
sys.path.append(r'C:\Users\dhuye\Desktop\C4E25\labs\lab3')
from calc import eval
from f_math_2 import create 

def generate_quiz():
    [x, y, op, result] = create()

    incorrect_result = result + randint(-5, 5)
    display_result = choice([result, incorrect_result])

    return x, y, op, display_result

def check_answer(x, y, op, result, user_choice):
    correct_result = eval(x, y, op)

    if correct_result == result:
        display = True
    else:
        display = False

    if user_choice == display:
        value = True
    else:
        value = False

    return value

