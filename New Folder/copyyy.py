fin=open("xiics12.txt","r")
fout=open("xiics4.txt","w")
for line in fin:
	word=line.split( )
	for i in word:
		for letter in i:
			if letter=='a' or letter=='A':
				fout.write(line)
fin.close( )
fout.close( )