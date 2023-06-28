def main():
	no = int(input("NO.OF NUMBERS "))
	ra = int(input("START RANGE "))
	re = int(input("END RANGE "))
	t = int(input("speed between each no. "))
	def sub():
		a=0
		i=0
		j=0
		k=0
		while i <= no :
			import random
			r = (random.randint(ra,re))
			from time import sleep
			print (r) ; sleep(t)
			a = a+r
			i = i+1
		else :
				print ("THE SUM IS")
				sleep (5)
				print (a)
	sub()
	j = int(input("Do you want to continue ?"))
main ()
while j ==1 :
	k = int (input ("With same values ?"))
	while k ==1 :
		sub()
	else :
		main()
else :
	print ("Thanks for using")