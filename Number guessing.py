from random import randint
def getno(a,l,m,n,p):
	v=0
	while a==None or a.isdigit() == False:
		if v>0:
	  	  print("Invalid "+l+p+", Enter a number")
		a=input("Enter "+n+m+" : ")
		v+=1
	else:
		a=int(a)
		return a #Hi guys
g=0
z="yes"
while z=="yes":
	if g ==0 :
		y=0
		a=None
		b=None
		b=getno(b,"upper ", "limit " , "upper " , "limit")
		a=getno(a,"lower ","limit" , "lower " , "limit")
		r=randint(a,b)
	x=None
	x=getno(x," input "," your"," guess " ,"")
	while x != r and y ==0:
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
		y=1
		print("You guessed in",g,"tries")
		g=0
		z=input("Do you want to play agaim ? (yes/no)").lower()
		while z not in ["yes","no"]:
			print("Enter a valid input")
			z=input("Do you want to play agaim ? (yes/no)").lower()
print("Thanks for playing , a program by TBA")
		