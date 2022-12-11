import mysql.connector as mydb
from tabulate import tabulate
con = mydb.connect(
	host = "localhost",
	user = 'tba',
	password="",
	database = "py")
cursor= con.cursor()
"""print (con)
print()
#try removing triple quotes to see connection id"""
q = None
def comit():
	cursor.execute(q)
	print(cursor.rowcount,"rows affected")
	con.commit()
def show():
	head=[]
	cursor.execute(q)
	column=(cursor.description)
	for i in column :
		head.append(i[0])
	print(tabulate(cursor,headers=head,tablefmt="grid"))
print("Welcome")
print("at any time type \"STOP\" to exit")
while q != "EXIT":
    try:
	    q=(input ("ENTER YOUR QUERY :  "))
	    b=(q.lower()).split()
	    if "show" in b[0] or "select" in b[0] or "desc" in b[0] :
	    	show()
	    elif "delete" in b[0] or "update" in b[0] or "insert" in b[0] or "drop" in b[0] :
	    	comit()
	    elif q == "STOP":
	    	break
	    else:
	    	cursor.execute(q)
    except Exception as e :
    	con.rollback()
    	print("error",e)
print("Thanks for using , a program by tba")
cursor.close()
con.close()