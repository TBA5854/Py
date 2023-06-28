x = int (input ("Start ?"))
while x ==1 :
	l = input ("Player 1 name :")
	k = input ("Player 2 name :")
	c = 0
	d = 0
	h = c or d
	while x == 1 :
		print ("LETS BEGIN THE GAME !")
		while h < 320 :
			a = int(input (l +" point is :"))
			b = int(input (k +" point is :"))
			c = c+a 
			d = d+b 
			h = c or d
			print (l,"total point is",c)
			print (k,"total point is",d)
		else :
			if c >= 320 :
				print (l+" lost , "+k+ " won")
				break
			if d >= 320 :
				print (k+" lost , "+l+ " won")
				break
	x = int(input("Do you want to play again ?"))
else :
	print ("Thanks for using my program")