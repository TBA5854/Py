import mysql.connector as mydb
con = mydb.connect(
	host = "localhost",
	user = 'u0_a18',
	password="",
	database = "py"
)
cursor= con.cursor()
print (con)
a= input("query ")
#x=("insert into s1 values (9,\"b\",7)")
try :
	db=cursor.execute(a)
	#db.commit()
	#x=mysql_affected_rows()
	#print(x)
	#db.commit()

except :
	con.rollback()
for i in cursor :
	print(i)
else :
	print("nonee")
con.close