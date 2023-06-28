import pickle
stufile=open("testing.dat","rb")
stud={}
found=False
print("Students Details")
try:
	while True:
		stud=pickle.load(stufile)
		if stud["Rollno"]==1003:
			print(stud)
			found=True
except:
	if found==False:
		print("Record not found")
	else:
		print("Record found")
stufile.close()