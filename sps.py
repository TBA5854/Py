import random
l=["Stone","Paper","Scissor"]
print("Welcome to a game of Stone , Paper or Scissor \nType exit to exit the program")
def assign():
	i=input("Stone , Paper or scissor ? ").lower()
	while i not in ("stone","paper","scissor","exit"):
		print("Invalid input , Try again")
		i=input("Stone , Paper or scissor ? ").lower()
	if i == "stone" :
		p=0
	elif i =="paper" :
		p=1
	elif i =="scissor" :
		p =2
	else:
		p=None
	c=random.randint(0,2)
	return p,c,i
def process():
	print("Computer played :",l[c],"\nYou played :",l[p])
	if p == c:
		print("Tie")
	if p==0 and c==1 :#r,p
		print ("Computer wins")
	if c==0 and p==1 :
		print ("Player wins")
	if p==1 and c==2 :
		print ("Computer wins")
	if c==1 and p==2 :
		print ("Player wins")
	if p==2 and c==0 :
		print ("Computer wins")
	if c==2 and p==0 :
		print ("Player wins")
o=1
while o==1:
	p=None
	while p not in range(0,3):
		p,c,i=assign()
		if i.lower() == "exit":
			o=0
			break
		process()
print("Thanks for playing , a program by tba")