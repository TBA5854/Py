import pdb
def view():
	global a
	for i in range(len(a)):
		print(a[i])
def push():
	global a
	a.append(input("Enter your number : "))
def pop():
	global a
	if a==[]:
		print("Stack is empty")
	else :
		b=a.pop(-1)
		print("deleted item :",b)
def peek():
	global a
	print("Peeked item :",a[-1])
def menu():
	global ch
	print("1 . Push \n2 . Pop \n3 . View\n4 . Peek\n5 . Quit")
	ch=input("Enter your choice : ")
	chck()
	#print(ch)
def chck():
	global ch
#	print(ch)
	if ch.isnumeric() == False:
		print("Invalid input , try again...")
		menu()
	if int(ch) not in range(1,6):
		print("Invalid choice , try again...")
		menu()
	ch=int(ch)
def opt():
	global ch
	if ch == 1:
		push()
	if ch == 2:
		pop()
	if ch==3:
		view()
	if ch==4:
		peek()
a=[]
while True:
	#pdb.set_trace()
	menu()
	opt()
	if ch==5:
		break
print("Thanks for using the program , a program by tba")