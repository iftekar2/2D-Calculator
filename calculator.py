from tkinter import *

def button_presse(num): #This section is for all the buttons that we have like 1, 2, +, -

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)
    

def equal():
    global equation_text

    #The try and except are used to catch any error that might occurr
    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
    
    except ZeroDivisionError: 
        equation_label.set("Arithmetic Error")

        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""

#This section is going to create the grap for the calculator. 
window = Tk()

window.geometry("500x500")
window.title("Calculator")

equation_text = ""

equation_label = StringVar()

#This will hold our expression that we want to celculate
label = Label(window, textvariable=equation_label,font=('consolas',20), bg="white", width=24, height=2)
label.pack()

#This section will hold all our buttons like + - ect..abs
frame = Frame(window)
frame.pack()

#This section adds buttons to numbers like 1, 2, 3 ect...
button1 = Button(frame, text = 1, height = 4, width = 9, font = 35, command = lambda: button_presse(1))
button1.grid(row = 0, column = 0)

button2 = Button(frame, text = 2, height = 4, width = 9, font = 35, command = lambda: button_presse(2))
button2.grid(row = 0, column = 1)

button3 = Button(frame, text = 3, height = 4, width = 9, font = 35, command = lambda: button_presse(3))
button3.grid(row = 0, column = 2)

button4 = Button(frame, text = 4, height = 4, width = 9, font = 35, command = lambda: button_presse(4))
button4.grid(row = 1, column = 0)

button5 = Button(frame, text = 5, height = 4, width = 9, font = 35, command = lambda: button_presse(5))
button5.grid(row = 1, column = 1)

button6 = Button(frame, text = 6, height = 4, width = 9, font = 35, command = lambda: button_presse(6))
button6.grid(row = 1, column = 2)

button7 = Button(frame, text = 7, height = 4, width = 9, font = 35, command = lambda: button_presse(7))
button7.grid(row = 2, column = 0)

button8 = Button(frame, text = 8, height = 4, width = 9, font = 35, command = lambda: button_presse(8))
button8.grid(row = 2, column = 1)

button9 = Button(frame, text = 9, height = 4, width = 9, font = 35, command = lambda: button_presse(9))
button9.grid(row = 2, column = 2)

button0 = Button(frame, text = 0, height = 4, width = 9, font = 35, command = lambda: button_presse(0))
button0.grid(row = 3, column = 0)

#This section will hold the signs like +, -, x, ect..
plus = Button(frame, text ="+", height = 4, width = 9, font = 35, command = lambda: button_presse("+"))
plus.grid(row = 0, column = 3)

minus = Button(frame, text ="-", height = 4, width = 9, font = 35, command = lambda: button_presse("-"))
minus.grid(row = 1, column = 3)

multiply = Button(frame, text ="*", height = 4, width = 9, font = 35, command = lambda: button_presse("*"))
multiply.grid(row = 2, column = 3)

devide = Button(frame, text ="/", height = 4, width = 9, font = 35, command = lambda: button_presse("/"))
devide.grid(row = 3, column = 3)

decimal = Button(frame, text =".", height = 4, width = 9, font = 35, command = lambda: button_presse("."))
decimal.grid(row = 3, column = 2)

equal = Button(frame, text ="=", height = 4, width = 9, font = 35, command = equal)
equal.grid(row = 3, column = 1)

#This button will clear wverying that we calculated previously
clear = Button(window, text ="Clear", height = 3, width = 12, font = 35, command = clear)
clear.pack()


window.mainloop()