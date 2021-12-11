import tkinter as tk
from tkinter import Canvas
import random as r
import inspect

# Creates UI size and disables resizing
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.geometry("210x350")
root.iconbitmap("icon.ico")

startpointer = 0    # Index of the first value in the list to show on the display
endpointer = 15     # Index of the last value in the list to show on the display
x = ""              # x is the value that will be displayed

# Places down nothing as whenever display called it needs to place destroy the text first
text = tk.Label(text= "" ,font=(25))
text.place(x=20,y=35)

backp = tk.Label(root,text ='<-0')
backp.place(x=50,y=35)

forw = tk.Label(root,text ='0->')
forw.place(x=50,y=35)


# Takes a value or operator and adds it onto the expression
def totalexpression(num):
    global x
    if len(x) == 0:
        x = x + str(num)
    elif len(x) > 0:
        if not(x[-1] in ".+-*/" and num in ".+-*/"):
            x = x + str(num)
        else:
            x = x
    display(x) 

# Displays any expression onto the calculator screen
def display(displayx):
    # Declares global as they need to be overrided for all the functions to see
    global startpointer
    global endpointer
    global text
    global backp
    
    length = len(displayx)
   
 
    caller = inspect.stack()[1][3]  # Checks if the functions calling are the arrow keys
    # If the caller of this function is the arrow functions then disable the pointer assignment
    if caller != "bArrow" and caller != "fArrow":
        if length >= 15:
            endpointer = length
            startpointer = length-15
    bval = len(displayx[:startpointer])
    fval = len(displayx[endpointer:])

    # Shortens and adds dots to show that the number calculated is bigger than can be displayed

    displayx = displayx[startpointer:endpointer]
  
    print(length, startpointer, endpointer)
    # Destroys whatever expression is displayed on calculator and places new expression
    text.destroy()
    text = tk.Label(text=displayx,font=(25))
    text.place(x=20,y=35)

    backp.destroy()
    backp = tk.Label(text= ("<-" + str(bval)) )
    backp.place(x=12,y=67)

    forwp = tk.Label(text = (str(fval) + '->'))
    forwp.place(x=165,y=67)

# Deletes last element in the expression
def delete(num):
    global x
    x = num[:-1]
    display(x)

# Deletes the whole expression
def AC(num):
    global startpointer
    global endpointer
    global x
    startpointer = 0 
    endpointer = 15
    x = num 
    x = ""
    display(x)

# Change start and end pointers to simulate navigating forward through expression
def fArrow(x):
    global startpointer
    global endpointer
    
    if len(x) > 15 and  endpointer < len(x):
        startpointer+=1
        endpointer+=1
        display(x)

# Change start and end pointers to simulate navigating backwards through expression
def bArrow(x):
    global startpointer
    global endpointer
    if len(x) > 15 and (startpointer-1) >= 0:
        startpointer-=1
        endpointer-=1
        display(x)

# Calculate the final expression
def calculate(num):
    global x
    try:
        answer = str(eval(num))

    except Exception as e:
        answer = "ERROR"
    x = answer
    display(x)

# If a letter is pressed on the keyboard is pressed run the corresponding function for that key
def keyPress(event,x):
    key = event.char
    
    for i in "1234567890+-*/().":
        if key == i:
            totalexpression(i)
    
    if key == ">":
        fArrow(x)
    
    elif key == "<":
        bArrow(x)
    
    elif key.lower() == "a":
        AC(x)
    
    elif key == "=":
        calculate(x)

def backspace(event,x):
    delete(x)

def enter(event,x):
    calculate(x)

def left(event,x):
    bArrow(x)

def right(event,x):
    fArrow(x)

# Detect keyboard input and call the corresponding function
root.bind("<KeyPress>", lambda event: keyPress(event,x))
root.bind("<BackSpace>",lambda event: backspace(event,x))
root.bind("<Return>",lambda event: enter(event,x))
root.bind("<Left>",lambda event: left(event,x))
root.bind("<Right>",lambda event: right(event,x))




# Declaring all of the elements on screen

buttonDot = tk.Button(text=".", command = lambda : totalexpression("."))
buttonDot.place(x = 10, y = 300, width=40, height=40)

button0 = tk.Button(text="0", command = lambda : totalexpression(0))
button0.place(x = 60, y = 300, width=40, height=40)

buttonDel = tk.Button(text="⌫" , command = lambda: delete(x))
buttonDel.place(x = 110, y = 300, width=40, height=40)

buttonEq = tk.Button(text="=", command = lambda: calculate(x))
buttonEq.place(x = 160, y = 300, width=40, height=40)

# New row

button1 = tk.Button(text="1", command = lambda : totalexpression(1))
button1.place(x = 10, y = 250, width=40, height=40)

button2 = tk.Button(text="2", command = lambda : totalexpression(2))
button2.place(x = 60, y = 250, width=40, height=40)

button3 = tk.Button(text="3", command = lambda : totalexpression(3))
button3.place(x = 110, y = 250, width=40, height=40)

buttonAdd = tk.Button(text="+", command = lambda : totalexpression("+"))
buttonAdd.place(x = 160, y = 250, width=40, height=40)

# New row

button4 = tk.Button(text="4", command = lambda : totalexpression(4))
button4.place(x = 10, y = 200, width=40, height=40)

button5 = tk.Button(text="5", command = lambda : totalexpression(5))
button5.place(x = 60, y = 200, width=40, height=40)

button6 = tk.Button(text="6", command = lambda : totalexpression(6))
button6.place(x = 110, y = 200, width=40, height=40)

buttonSub = tk.Button(text="-", command = lambda : totalexpression("-"))
buttonSub.place(x = 160, y = 200, width=40, height=40)

#New row

button7 = tk.Button(text="7", command = lambda : totalexpression(7))
button7.place(x = 10, y = 150, width=40, height=40)

button8 = tk.Button(text="8", command = lambda : totalexpression(8))
button8.place(x = 60, y = 150, width=40, height=40)

button9 = tk.Button(text="9", command = lambda : totalexpression(9))
button9.place(x = 110, y = 150, width=40, height=40)

buttonMul = tk.Button(text="*", command = lambda : totalexpression("*"))
buttonMul.place(x = 160, y = 150, width=40, height=40)

#New row

buttonAC = tk.Button(text="AC", command = lambda: AC(x))
buttonAC.place(x = 10, y = 100, width=40, height=40)

buttonBArrow = tk.Button(text="<-", command = lambda: bArrow(x))
buttonBArrow.place(x = 60, y = 100, width=20, height=40)

buttonFArrow = tk.Button(text="->", command = lambda: fArrow(x))
buttonFArrow.place(x = 80, y = 100, width=20, height=40)

buttonRBracket = tk.Button(text=")", command = lambda : totalexpression(")"))
buttonRBracket.place(x = 130, y = 100, width=20, height=40)

buttonLBracket = tk.Button(text="(", command = lambda : totalexpression("("))
buttonLBracket.place(x = 110, y = 100, width=20, height=40)

buttonDiv = tk.Button(text="/", command = lambda : totalexpression("/"))
buttonDiv.place(x = 160, y = 100, width=40, height=40)
1
# Draw the calculator screen
canvas= Canvas(root, width=250, height=90)
canvas.create_line(10, 90, 200, 90)
canvas.create_line(10, 90, 10, 10)
canvas.create_line(10, 10, 200, 10)
canvas.create_line(200, 10, 200, 91)
canvas.pack()

root.mainloop()