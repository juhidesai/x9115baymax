def check_em(a, b):
    if a < b:
        c = a+b
        d = c+c/2
        e = 2
    else:
        c = a-b
    if c%2 == 0:
        print("Even")
    else:
        print("Odd")
