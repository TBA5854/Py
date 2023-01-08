import tkinter as tk
import mysql.connector as mydb
from tabulate import tabulate
con = mydb.connect(
	host = "localhost",
	user = 'tba',
	password="",
	database = "py")
cursor= con.cursor()
# Create the main window
window = tk.Tk()
def comit():
	global op
	cursor.execute(q)
	op = (cursor.rowcount,"rows affected")
	con.commit()
def show():
	global op
	head=[]
	cursor.execute(q)
	column=(cursor.description)
	for i in column :
		head.append(i[0])
	op=(tabulate(cursor,headers=head,tablefmt="grid"))
history=[]
# Create a function to get input from the user
def get_input():
    global q
    global op
    # Get the input from the input field
    input_text = input_field.get()
    try:
	    q=input_text#(input ("ENTER YOUR QUERY :  "))
	    #print(q)
	    b=(q.lower()).split()
	    if "show" in b[0] or "select" in b[0] or "desc" in b[0] :
	    	show()
	    elif "delete" in b[0] or "update" in b[0] or "insert" in b[0] or "drop" in b[0] :
	    	comit()
	    else:
	    	cursor.execute(q)
	    	op="Executed"
    except Exception as e :
    	con.rollback()
    	op = (e)
    
    # Display the input in a label widget
    #   output_label['text'] = "{}".format(op)
    history.append((input_text,op))
    text.configure(state="normal")
    text.delete(1.0,tk.END)
    text.insert(tk.END,op)
    text.configure(state="disabled")
def show_history():
    # Create a new window to display the history
    history_window = tk.Toplevel(window)
    # Add a scrollbar to the window
    scrollbar = tk.Scrollbar(history_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # Add a listbox widget to the window to display the history
    history_list = tk.Listbox(history_window, yscrollcommand=scrollbar.set)
    for item in history:
        history_list.insert(tk.END, f"Input: {item[0]} \n Output: {item[1]}")
    history_list.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=history_list.yview)

# Create an input field
output_label = tk.Label(window, text='Welcome to\nQueries from python')
output_label.pack()
input_field = tk.Entry(window)
input_field.pack()

# Create a button to get the input
get_input_button = tk.Button(window, text='Submit Query', command=get_input)
get_input_button.pack()

# Create a label to display the output
#output_label = tk.Label(window, text='Output will appear here',justify="left")
#output_label.pack()
text = tk.Text(window,height=39, width=43) 
text.pack()

history_button = tk.Button(window, text="History", command=show_history)
history_button.pack()

quit_button=tk.Button(window,text="Quit",command=window.destroy)
quit_button.pack()
# Run the Tkinter event loop
window.mainloop()
