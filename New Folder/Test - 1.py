while True :
	try:
		a=float(int(input("Enter your first number:")))
		b=float(int(input("Enter your second number")))
	while a or b < 0 :
			print ("Enter a valid number")
			a=float(input("Enter your first number:"))
			b=float(input("Enter your second number"))
		p=a
		s=b
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
		print ("Do you want to use my program again 	?")
		print ( "0 for no and 1 for yes")
		h = float(input ( ))
		while h==1 :
			a=float(input("Enter your first number:"))
			b=float(input("Enter your second number"))
			p=a
			s=b
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
				print( "0 for no and 1 for yes")
				h=float(input ())
			else :
				print ("thanks for using my program")
except ValueError :
	print ("Enter only numbers")