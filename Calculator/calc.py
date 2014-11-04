from Tkinter import *
import pdb

root = Tk()
root.geometry("460x460") # How big in the screen
calc = Frame(root)
calc.grid()

# Entry widget is used to accept a single-line text strings from the user
# w = Entry(master, option...)
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row=0, column=0, columnspan=6, pady=5)
text_box.insert(0, "0") # Initial value is 0

numbers = "789456123"
inp = "0"

#Action to be taken when a number is pressed
def num_press(num):
	global inp
	val = text_box.get()
	if inp and inp != "0":
		# Special cases
		# If . is alreadt there in input and new input is .
		if '.' in inp and (str(num) == "."):
			return

		# If 0 is already there, ignore it
		if (inp == "0" and str(num) == "0"):
			return

		inp = inp + str(num)
	else:
		# if '.' is the first character inserted, then retain 0
		if (str(num) == "."):
			inp = "0."
		else:
			inp = str(num)	

	# Insert the computed inp in the text box
	text_box.delete(0, END)
	text_box.insert(0, inp)

# Action to be taken when C (clear) button is pressed
def zero_press():
	global inp
	inp = "0"
	print "Inserting C"
	text_box.delete(0, END)
	text_box.insert(0, inp)

# Action to be taken when percentage button is pressed
def percentage_press():
	print "Percentage pressed"
	
bttn = []
i = 0
for j in range(1,4):
	for k in range(3):
		bttn.append(Button(calc, text = numbers[i]))
		bttn[i].grid(row=j, column=k, pady=5)
		# The difference here is that, the particular lambda function
		# is a method which calls another method which passes an integer
		# The parameter passed is x. x needs to have a value which is
		# numbers[i]
		bttn[i]["command"] = lambda x = numbers[i]: num_press(x) 
		i = i + 1
		

# C Button
cbutt = Button(calc, text = "C", command = zero_press)
cbutt.grid(row=1, column=3, pady=5)

# . Button
dbutt = Button(calc, text = ".", command = lambda: num_press("."))
dbutt.grid(row=4, column=1, pady=5)

# Number 0
zero_butt = Button(calc, text = "0", command = lambda: num_press(0))
zero_butt.grid(row=4, column=0, pady = 5)

# % Button
per_butt = Button(calc, text = "%", command = percentage_press)
per_butt.grid(row=4, column=2, pady=5)

print bttn


#pdb.set_trace()		
root.title("Calculator")
root.mainloop()
