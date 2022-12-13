from random import randint
a=None
b=None
a=input("Enter upper limit : ")
b=input("Enter lower limit : ")
while a==None or a.isdigit() == False:
    print("Invalid upper limit , Enter a number")
    a=input("Enter upper limit : ")
else:
	a=int(a)
#Hi guys !
while b==None or b.isdigit() == False:
    print("Invalid lower limit , Enter a number")
    b=input("Enter lower limit : ")
else:
	b=int(b)
g=0
r=randint(b,a)
			#print(r)
while True:
	x=int(input("Enter your guess : "))
	while x != r:
		x=int(input("Enter your guess : "))
		if x > r :
			print("You guessed higher , Try again")
			g+=1
			continue
		else:
			print("You guessed lower , Try again")
			g+=1
			continue
	else :
		print("You guessed right")
		g+=1
		print("You guessed in",g,"tries")
		print("Thanks for playing , a program by TBA")
		quit()
		