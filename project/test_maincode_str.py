def check_em_too(l,m,n,o):
	a = len(l)
	b = len(m)
	c = len(n)
	d = len(o)
	
	print " "
	print "lengths - [ "+ str(a) + " " + str(b) + " " + str(c) + " " + str(d) + "  ]", 
	print "you are in ",
	if a >= 5 and a <= 10:
		print "a",
		a = a + 1
		
	if b >= 10 and b <= 15:
		print "b",
		b = b + 2
		
	if c >= 15 and c <= 20:
		print "c",
		c = c + 3
		
	if d >= 20 and d <= 25:
		print "d",
		d = d + 4