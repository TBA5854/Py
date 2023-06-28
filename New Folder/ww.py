import csv
f=open("test.csv","r",newline="\r\n")
ireader=csv.reader(f)
#ino=(input("Enter the itemno to be searched"))
#found=False
for i in ireader:
    print(i)
    if i[0]==ino:
        print(i)
  #      found=True
#if found==False:
 #   print("Itemno is not found")
else:
    print("Itemno is found")
f.close()