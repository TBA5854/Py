x=int(input())
a = x
while x > 4:
	z = int(input())
	while z == 1:
		if a %2 ==0:
			a= a/2
		if a %2 ==1 :
			a= a*3+1
		if a < 5 :
			print (x,a)
			x = x+1