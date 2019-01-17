from random import randint, choice
from calc import eval # import module (calc.eval)/from module import eval

# Sinh bieu thuc:
def create():
    op = choice(["+", "-", "*", "/"])
    x = randint(0, 10)
    if op != "/":
        y = randint(0, 10)
    else:
        y = randint(1, 10)

    s = eval(x, y, op)
    
    return (x, y, op, s)

if __name__ == '__main__':
    [x, y, op, s] = create()

    s2 = s + randint(-5, 5)
    r = choice([s, s2])

    print(x, op, y, "=", r)

    if r == s:
        correct = "Y"
    else:
        correct = "N"

    ans = input("Y/N: ").upper()
    if ans == correct:
        print("Yay")
    else:
        print("Nay")