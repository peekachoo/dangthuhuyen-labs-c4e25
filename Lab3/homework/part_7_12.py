# Exercise7-8:
def remove_dollar_sign(s):
    snew = s.replace("$", "")
    return snew

if __name__ == '__main__':
    string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
    if string_with_no_dollars == "80% percent of life is to show up":
        print("Your function is correct")
    else:
        print("Oops, there's a bug")


# Exercise9-10:
def get_even_list(l):
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
    return even

if __name__ == '__main__':
    even_list = get_even_list([1, 2, 5, 9, -10, 6])

    if set(even_list) == set([2, -10, 6]): #unordered data
        print("Your function is correct")
    else:
        print("Ooops, bugs detected")


# Exercise11-12:
def is_inside(x, y):
    zone1 = y[0] + y[2]
    zone2 = y[1] + y[3]

    if (y[0] < x[0] < zone1) and (y[1] < x[1] < zone2):
        r = True
    else:
        r = False
    return r

if __name__ == '__main__':
    print(is_inside([200, 120], [140, 60, 100, 200]))
    print(is_inside([100, 120], [140, 60, 100, 200]))
        

