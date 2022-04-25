from tkinter import *

win = Tk()
win.title("Calculator")
win.config(bg = "gray")

entry=Entry(win,width=35,borderwidth=5)
entry.grid(row=0,column=0,columnspan=3)

def leo(number):
    first = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(first)+str(number))


def clear():
    entry.delete(0,END)

def add():
    first_number=entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0,END)

def minus():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0,END)


    
def equal():
    second_number = entry.get()
    entry.delete(0,END)
    if math=="addition":
        entry.insert(0,f_num + int(second_number))
    if math == "subtraction":
        entry.insert(0,f_num - int(second_number))
    if math == "multiply":
        entry.insert(0,f_num * int(second_number))
    if math == "divide":
        entry.insert(0,f_num / int(second_number))

def multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    entry.delete(0,END)

def divide():
    first_number = entry.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    entry.delete(0,END)

        
                 
    
button_1 = Button(text="1",padx=30,pady=20,command=lambda:leo(1))
button_2 = Button(text="2",padx=30,pady=20,command=lambda:leo(2))
button_3 = Button(text="3",padx=30,pady=20,command=lambda:leo(3))
button_4 = Button(text="4",padx=30,pady=20,command=lambda:leo(4))
button_5 = Button(text="5",padx=30,pady=20,command=lambda:leo(5))
button_6 = Button(text="6",padx=30,pady=20,command=lambda:leo(6))
button_7 = Button(text="7",padx=30,pady=20,command=lambda:leo(7))
button_8 = Button(text="8",padx=30,pady=20,command=lambda:leo(8))
button_9 = Button(text="9",padx=30,pady=20,command=lambda:leo(9))
button_0 = Button(text="0",padx=30,pady=20,command=lambda:leo(0))
button_multiply = Button(text="*",padx=30,pady=20,command=multiply)
button_dividing = Button(text="/",padx=30,pady=20,command=divide)
button_minus = Button(text="-",padx=30,pady=20,command=minus)
button_AC = Button(text="AC",padx=30,pady=20,command=clear)
button_equal = Button(text="=",padx=30,pady=20,command=equal)
button_plus = Button(text="+",padx=30,pady=20,command=add)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_plus.grid(row=4,column=1)
button_minus.grid(row=4,column=2)
button_AC.grid(row=5,column=0)
button_equal.grid(row=5,column=1)
button_multiply.grid(row=5,column=2)
button_dividing.grid(row=6,column=0)
