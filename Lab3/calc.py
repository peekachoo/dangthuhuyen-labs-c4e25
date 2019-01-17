# # input:
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# f = input("Enter operator (+/-/*/:): ")

# # process:
# if f == "+":
#     s = x + y
# elif f == "-":
#     s = x - y
# elif f == "*": 
#     s = x * y
# else:
#     s = x / y

# # output:    
# print(s)

        # Functions:

        # def sayHi(n): # n - function parameters/arguments
        #     print("Hi") # function body
        #     print("Hi", n)
        #     print("Bye bye")
        # sayHi("Quan")
        # sayHi("Huyen")

        # def add(x, y):
        #     s = x + y
        #     return s # co return: fruitful function, khong return: non fruitful

        # s = add(4, 5) # khong bat buoc bien phai la s (bien chua != bien trong def)
        # print(s)

        # t = add(3, 4)
        # print(t)

def eval(x, y, op):
    s = 0

    if op == "+":
        s = x + y
    elif op == "-":
        s = x - y
    elif op == "*": 
        s = x * y
    else:
        s = x / y
    
    return s

# a = int(input("a = "))
# b = int(input("b = "))
# op = input("op = ")

# s = eval(a, b, op)
# print(s)
