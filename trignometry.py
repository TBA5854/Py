from math import sin
from math import cos
from math import tan
from math import radians
import os
from time import sleep
x=(1,2,3,4,5,6)
y=(0,1)
def welcome ():
	print ("WELCOME TO THE PROGRAM")
	print ("		-by TBA")
	print ("Your options are :")
	print ("1.Sine")
	print("2.Cosine")
	print ("3.Tangent")
	print("4.Cosecan")
	print("5.Secan")
	print("6.Cotangent")
	print("\n\n")
	op = int(input("Enter your option : "))
	return op
def getno():
	b=radians(int(input("Enter your number : ")))
	return b
def sine(b):
	a=sin(b)
	return a
def cosine(b):
	a=cos(b)
	return a
def tang(b):
	a=tan(b)
	return a
def process(b,op):
	if op ==1:
		print(round(sine(b),2))
	elif op ==2:
		print(round(cosine(b),2))
	elif op ==3:
		print(round(tang(b),2))
	elif op ==4:
		print(round(1/sine(b),2))
	elif op ==5:
		print(round(1/cosine(b),2))
	elif op ==6:
		print(round(1/tang(b),2))
def continuee():
	r=int(input(r"Do you want to use again ? (0/1) "))
	while r not in range (0,2):
		print("Invalid input , Try again")
		r=int(input(r"Do you want to use again ? (0/1) "))
	return r
r=1
while r ==1:
	if os.name=="posix":
		os.system("clear")
	else:
		os.system("cls")
	op = welcome()
	print (op)
	while op not in range(1,7):
		print("Try again")
		sleep(5)
		os.system("clear")
		op = welcome()
	b=getno()
	process(b,op)
	r=continuee()
else :
	print ("\nThanks for using the program \nbyeeee :)")
	
