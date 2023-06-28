import androidhelper
no = int(input("NO.OF NUMBERS "))
ra = int(input("START RANGE "))
re = int(input("END RANGE "))
t = int(input("speed between each no. "))
i =0
a=0
while i <= no :
	import random
	r = (random.randint(ra,re))
	from time import sleep
	print (r) ; sleep(t)
	droid.ttsSpeak(r)
	a = a+r
	i = i+1
else :
		print ("THE SUM IS")
		sleep (5)
		print (a)