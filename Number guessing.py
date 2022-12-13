from random import randint
a=None
b=None
def getno(a,l,m,n,p):
	v=0
	while a==None or a.isdigit() == False:
		if v>0:
	  	  print("Invalid "+l+p+", Enter a number")
		a=input("Enter "+n+m+" : ")
		v+=1
	else:
		a=int(a)
		return a
b=getno(b,"upper ", "limit " , "upper " , "limit")
a=getno(a,"lower ","limit" , "lower " , "limit")
#Hi guys !
g=0
r=randint(a,b)
while True:
	x=None
	x=getno(x," input "," your"," guess " ,"")
	while x != r:
		if x > r :
			print("You guessed higher , Try again")
			g+=1
			
		else:
			print("You guessed lower , Try again")
			g+=1
			
		x=int(input("Enter your guess : "))
	else :
		print("You guessed right")
		g+=1
		print("You guessed in",g,"tries")
		print("Thanks for playing , a program by TBA")
		quit()
		