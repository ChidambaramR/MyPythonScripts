from Tkinter import *

root = Tk()
root.geometry("160x160")
calc = Frame(root)
calc.grid()

text_box = Entry(calc, justify=RIGHT)
text_box.grid(row=0, column=0, columnspan=3, pady=5)
numbers = "789456123"

bttn = []
i = 0
for j in range(1,4):
	for k in range(3):
		bttn.append(Button(calc, text = numbers[i]))
		bttn[i].grid(row=j, column=k, pady=5)
		bttn[i]["command"] = num_press(numbers[i])
		i = i + 1
		
		
root.title("Calculator")
root.mainloop()
