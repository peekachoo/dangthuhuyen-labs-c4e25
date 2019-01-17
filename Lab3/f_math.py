from random import randint, choice

# Sinh bieu thuc:
x = randint(0, 10)
y = randint(0, 10)
s = x + y

e = randint(-5, 5)
s2 = s + e

result = [s, s2]
r = choice(result)
print(x, "+", y, "=", r)

if r == s:
    correct = "Y"
else:
    correct = "N"

ans = input("Y/N: ").upper()
if ans == correct:
    print("Yay")
else:
    print("Nay")