import pickle
f=open("testing.dat","wb")
s={}
ans="y"
while ans=="y":
	rno=int(input("Enter roll number:"))
	name=input("Enter name:")
	mark1=int(input("Enter English mark:"))
	mark2=int(input("Enter Maths mark:"))
	mark3=int(input("Enter CS mark:"))
	s["Rollno"]=rno
	s["Name"]=name
	s["Mark1"]=mark1
	s["Mark2"]=mark2
	s["Mark3"]=mark3
	pickle.dump(s,f)
	ans=input("Do u want to append more records?(y/n)...?")
f.close()