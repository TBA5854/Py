file=open(r"0\Python\hi.txt","a+")
file.write("helloooooo\n")
file.seek(0)
a=file.read()
print(a)
file.close()