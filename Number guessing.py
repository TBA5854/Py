from random import randint
def geta():
	a=input("Enter upper limit : ")
	return a
def getb():
	b=input("Enter lower limit : ")
	return b
g=0
a=geta()
b=getb()
while True:
	if a.isnumeric():
		c=int(a)
		if b.isnumeric():
			d=int(b)
			r=randint(c,d)
			#print(r)
			while True:
				x=int(input("Enter your guess : "))
				if x==r :
					print("You guessed right")
					g+=1
					print("You guessed in",g,"tries")
					print("Thanks for playing , a program by TBA")
					quit()
				elif x > r :
					print("You guessed higher , Try again")
					g+=1
					continue
				else:
					print("You guessed lower , Try again")
					g+=1
					continue
		else:
			print("Invalid lower limit , Enter a number")
			b=getb()
			continue
	else:
		print("Invalid upper limit , Enter a number")
		a=geta()
		continue
