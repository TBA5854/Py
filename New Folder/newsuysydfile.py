p=float(input("Enter your first number:"))
s=float(input("Enter your second number"))
a=p
b=s
d = a*b
if a<b :
	c = a
	a = b
	b = c
q = a // b
r = a % b
while r!=0 :
	a = b
	b = r
	q = a // b
	r = a % b
	print ("a")
	print (a)
	print (b)
	print (q)
	print (r)
else :
	print ("HCF of the numbers is :")
	print (b)
	print ("LCM of the numbers is :")
	print (d/b)
print ("Do you want to use my program again ?")
print ( "0 for no and 1 for yes")
h = float(input ( ))
while h==1 :
	return p