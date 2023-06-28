while True:
  try:
    a = int(input("Enter first integer number: "))
    b = int(input("Enter second integer number: "))
    break
  except ValueError:
      print("Please input integer only...")  
      continue
p=a
s=b
d = a*b
if a<b :
	c = a
	a = b
	b = c
q = a // b
r = a % b
while r!=0 :
	a = b
	b = r
	q = a // b
	r = a % b
else :
	print ("HCF of the numbers is :")
	print (b)
	print ("LCM of the numbers is :")
	print (d/b)
print ("Do you want to use my program again ?")
print ( "0 for no and 1 for yes")
while True:
  try:
    h = float(input ( ))
    break
  except ValueError:
      print("Please input integer only...")  
      continue	
while h==1 :
	while True:
	  try:
	    a = int(input("Enter first integer number: "))
	    b = int(input("Enter second integer number: "))
	    break
	  except ValueError:
	      print("Please input integer only...")  
	      continue
	p=a
	s=b
	d = a*b
	if a<b :
		c = a
		a = b
		b = c
	q = a // b
	r = a % b
	while r!=0 :
		a = b
		b = r
		q = a // b
		r = a % b
	else :
		print ("HCF of the numbers is :")
		print (b)
		print ("LCM of the numbers is :")
		print (d/b)
	print ("Do you want to use my program again ?")
	print( "0 for no and 1 for yes")
	while True:
	  try:
	    h = float(input ( ))
	    break
	  except ValueError:
	      print("Please input integer only...")  
	      continue
else :
	print ("thanks for using my program")