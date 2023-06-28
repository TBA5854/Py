import csv
f=open("test.csv","r",newline="\r\n")
ireader=csv.reader(f)
p=[*ireader]
print(ireader)
print(*ireader)
for i in ireader:
    print(i)
    if i[0]==1:
        print(i)
        found=True
f.close()