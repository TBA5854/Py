def circle(r):
    area=3.14*(r**2)
    print(" the area of the circle is:",area)

def rectangle(l,b):
    R=l*b
    print("the area of rectangleis:",R)

def triangle(b,h):
    R=0.5*b*h
    print("the area of triangle:",R)
def menu():
	global ch
	print("1.area of circle")
	print("2.area of rectangle")
	print("3.area of triangle")
	ch=int(input("your choice : "))
def sel():
	if ch==1:
	     a=int(input("enter radius"))
	     circle(a)
	elif ch ==2:
	      l=int(input("enter length"))
	      b=int(input("enter breath"))
	      rectangle(l,b)
	elif ch==3:
	       b=int(input("enter base"))
	       h=int(input("height"))
	       triangle(h,b)
	else:
         print("try again")
print("Type STOP to exit")
while True:
	menu()
	sel()
	if ch =="STOP":
		break