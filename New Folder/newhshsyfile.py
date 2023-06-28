x = int (input ("Start ?"))
while x ==1 :
	c = 0
	d = 0
	h = c or d
	print ("LETS BEGIN THE GAME !")
	while c < 360 :
		while d < 360 :
			while c < 360 :
				a = int(input (l +" point is :"))
				b = int(input (k +" point is :"))
				c = c+a 
				d = d+b 
				print (l,"total point is",c)
				print (k,"total point is",d)
			else :
				if 1 ==1 : 
					print (l+" lost , "+k+ " won")
					break
		else :
			print (k+" lost , "+l+ " won")
			break
	break
	x = int(input("Do you want to play again ?"))
else :
	Print ("Thanks for using my program")