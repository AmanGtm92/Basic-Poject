# Python Tkinter GUI based "LOVE CALCULATOR"

from tkinter import *
import random
root = Tk()

root.geometry('400x240')

root.title('Love Calculator????')



def calculate_love():

	st = '0123456789'

	digit = 2
	temp = "".join(random.sample(st, digit))
	result.config(text=temp)


heading = Label(root, text='Love Calculator - How much is he/she into you')
heading.pack()


slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()


slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="Calculate", height=1,
			width=7, command=calculate_love)
bt.pack()


result = Label(root, text='Love Percentage between both of You:')
result.pack()


root.mainloop() 