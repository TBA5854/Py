import csv
f=open("test.csv","a")
rec=[ ]
iwriter=csv.writer(f)
print('Item Details')
iwriter.writerow(["itemno","iname","quantity","price"])
for i in range(5):
    itemno=int(input("Enter itemno:"))
    iname=input("Enter item name:")
    quantity=int(input("Enter quantity"))
    price=int(input("Enter price"))
    l=[itemno,iname,quantity,price]
    rec.append(l)
    iwriter.writerow(l)
#    print(l)
#print(rec)
#iwriter.writerows(rec)
f.close()
