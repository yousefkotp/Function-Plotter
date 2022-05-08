from tkinter import *
import tkinter.messagebox
import matplotlib.pyplot as plt
from matplotlib import pylab

# space separated input for function help us deal with more than one digit number

#function to validate input
def validInput(x1,x2,func):
    #if entered max and min value is not a number
    func = func.split(" ")
    #to accept the negative numbers

    if not x1.lstrip("-").isdigit() or not x2.lstrip("-").isdigit():
        tkinter.messagebox.showerror("Error", "Please make sure you typed integer into minimum and maximum value")
        return False
    #if min value is empty
    if x1 == "":
        tkinter.messagebox.showerror("Error", "Please make sure you typed input into minimum value")
        return False
    #if max value is empty
    if x2 == "":
        tkinter.messagebox.showerror("Error", "Please make sure you typed input into maximum value")
        return False
    #if max is smaller than min value
    if x2<x1:
        tkinter.messagebox.showerror("Error","Maximum value can't be smaller than minimum value")
        return False
    #if function expression is empty
    if func=="":
        tkinter.messagebox.showerror("Error", "You entered empty function")
        return False

    #if function starts with operation
    if func[0] =="+" or func[0]=="-" or func[0]=="*" or func[0]=="/" or func[0]=="^":
        tkinter.messagebox.showerror("Error", "Please check the function you entered")
        return False
    #if function ends with operation
    if func[-1] =="+" or func[-1]=="-" or func[-1]=="*" or func[-1]=="/" or func[-1]=="^":
        tkinter.messagebox.showerror("Error", "Please check the function you entered")
        return False
    #if function has another letter other than x and numbers and operations
    for i in func:
        if i != "+" and i!="-" and i!="*" and i!="/" and i!="^" and not i.isdigit() and i !="x":
            tkinter.messagebox.showerror("Error", "Please check the function you entered")
            return False
    #if length of function is 1 and it is not a number or x
    if len(func)==1 and not func[0].isdigit() and func[0]!="x":
        tkinter.messagebox.showerror("Error", "Please check the function you entered")
        return False


    return True

#function to convert function from infix to postfix
def infixToPostfix(func):
    #declaring stack and the postfix expression which will be returned
    stack = []
    postfix = ""
    #putting the string representing number and operations into a list
    list = func.split(" ")
    for c in list:
        #if the character is digit or x, we put it immediately in postifx expression
        if c.isdigit() or c=="x":
            postfix += c
            postfix += " "
        else:
            #if character is operation, we pop the stack as long as its top has higher or equal priority to current charachter
            #each element popped is inserted into postfix expression
            while len(stack)!=0 and priority(c) <= priority(stack[-1]):
                postfix += stack.pop()
                postfix+=" "
            stack.append(c)

    #making sure the stack is empty
    while (len(stack)!=0):
        postfix += stack.pop()
        postfix+=" "

    #removing the last extra space
    postfix = postfix[:-1]
    return postfix

def priority(x):
    if x=='^':
        return 3
    elif x=='*' or x=='/':
        return 2
    elif x=='+' or x=='-':
        return 1

#function to evaluate postfix expression
def evaluatePostfix(func):
    stack =[]
    # separating postfix expression using space delimiter
    list = func.split(" ")
    for i in list:
        #if the character is digit, we put it in the stack
        #lstrip to make sure we handle negative numbers too
        if i.lstrip("-").isdigit():
            stack.append(i)
        else:
            #if it is operation, we pop last two elements of the stack and perform the operation on them
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(eval(val2, val1, i))
    #last element in the stack has the final result
    return int(stack.pop())
def eval(x,y,operation):        #this function evaluate the value of two numbers according to operation between them
    x = int(x)
    y = int(y)
    if operation=='+':
        return x+y
    elif operation=='-':
        return x-y
    elif operation=='*':
        return x*y
    elif operation=='/':
        return x/y
    elif operation=='^':
        return x**y

#action listner for button if clicked
def handle_plot():                 #action listener for plot function
    #retriving the entry into variables
    x1 = ent_x1.get()
    x2 = ent_x2.get()
    func = ent_func.get()

    #checking if the input is valid
    if (not validInput(x1, x2, func)):
        return

    #declaring our x and y to be used
    x = range(int(x1), int(x2) + 1)
    y = []

    for i in x:         #iterating from min to max value
        #calculating postfix expression for the function
        postfix = infixToPostfix(func)
        #replacing every 'x' in the postfix expression with its actual value
        postfix= postfix.replace("x",str(i))
        #adding f(x) to y list
        y.append(evaluatePostfix(postfix))

    #configuring our plot settings
    plt.plot(x,y,marker='o', markerfacecolor='black')
    #gcf -> grab current figure
    fig = pylab.gcf()
    #setting window title
    fig.canvas.manager.set_window_title('Function Plotter')
    #setting plot title
    plt.title("Plot of the function")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    #writing the exact point info
    for i_x, i_y in zip(x, y):
        plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
    #showing the plot
    plt.show()



#decalring window from tkinter
window = Tk()
window.title("Function Plotter")
#centralizing the window
window_height = 200
window_width = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#configuring the background of window
window.configure(bg = "#ffffff")

#configuring our canvas
canvas =Canvas(
    window,
    bg = "#ffffff",
    height = 200,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

#delaring image of the button
img0 = PhotoImage(file = f"img0.png")




#making the minimum value of x entry
ent_x1_img = PhotoImage(file =f"img_textBox0.png")
ent_x1_bg = canvas.create_image(
    352.5, 54.5,
    image = ent_x1_img)
ent_x1 = Entry(
    bd = 0,
    bg = "#e4e2e2",
    highlightthickness = 0)
ent_x1.place(
    x = 261.5, y = 45,
    width = 182.0,
    height = 17)

#making the maximum value of x entry
ent_x2_img = PhotoImage(file =f"img_textBox1.png")
ent_x2_bg = canvas.create_image(
    352.5, 94.5,
    image = ent_x2_img)
ent_x2 = Entry(
    bd = 0,
    bg = "#e4e2e2",
    highlightthickness = 0)
ent_x2.place(
    x = 261.5, y = 85,
    width = 182.0,
    height = 17)

#making the function entry
ent_func_img = PhotoImage(file =f"img_textBox2.png")
ent_func_bg = canvas.create_image(
    352.5, 132.5,
    image = ent_func_img)
ent_func = Entry(
    bd = 0,
    bg = "#e4e2e2",
    highlightthickness = 0)

ent_func.place(
    x = 261.5, y = 123,
    width = 182.0,
    height = 17)

#making the plot button
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = handle_plot,
    relief = "flat")

b0.place(
    x = 374, y = 155,
    width = 106,
    height = 45)

#configuring background settings
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    252.5, 75.5,
    image=background_img)

window.resizable(False, False)

#assigning enter key to the button
window.bind('<Return>', lambda event:handle_plot())

#put the focus on first entry
ent_x1.focus_set()
window.mainloop()
