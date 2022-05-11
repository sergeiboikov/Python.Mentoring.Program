def nod_function():
    x = int(input("Input the first number: "))
    y = int(input("Input the second number: "))

    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x if x != 0 else y


print(nod_function())
