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

def check_em_too(a,b,c,d):
	g = a + c + d*10
	if g > 100:
		e = 100
		f = e*b
		if f%2 == 0:
			print f
	else:
		f = g%22
		if f%2 != 0:
			print f
		else:
			print g
