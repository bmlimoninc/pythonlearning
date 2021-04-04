# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *
import math

# globally declare the expression variable
expression = ""

calculatorBGColor = "gray"
buttonBGColor = "black"
buttonFGColor = "gray"

buttonHeight = 2
buttonWidth = 7


# Function to update expressiom
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():

    try:

        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""
    except:

        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background=calculatorBGColor)

    # set the title of GUI window
    gui.title("Basic Calculator")

    # set the configuration of GUI window
    gui.geometry("270x270")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry panel in order to show  the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place them

    button1 = Button(gui, text=' 1 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(1), height=buttonHeight, width=buttonWidth)
    button1.grid(row=5, column=0)

    button2 = Button(gui, text=' 2 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(2), height=buttonHeight, width=buttonWidth)
    button2.grid(row=5, column=1)

    button3 = Button(gui, text=' 3 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(3), height=buttonHeight, width=buttonWidth)
    button3.grid(row=5, column=2)

    button4 = Button(gui, text=' 4 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(4), height=buttonHeight, width=buttonWidth)
    button4.grid(row=4, column=0)

    button5 = Button(gui, text=' 5 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(5), height=buttonHeight, width=buttonWidth)
    button5.grid(row=4, column=1)

    button6 = Button(gui, text=' 6 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(6), height=buttonHeight, width=buttonWidth)
    button6.grid(row=4, column=2)

    button7 = Button(gui, text=' 7 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(7), height=buttonHeight, width=buttonWidth)
    button7.grid(row=3, column=0)

    button8 = Button(gui, text=' 8 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(8), height=buttonHeight, width=buttonWidth)
    button8.grid(row=3, column=1)

    button9 = Button(gui, text=' 9 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(9), height=buttonHeight, width=buttonWidth)
    button9.grid(row=3, column=2)

    button0 = Button(gui, text=' 0 ', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press(0), height=buttonHeight, width=buttonWidth)
    button0.grid(row=6, column=1)

    plus = Button(gui, text=' + ', fg=buttonFGColor, bg=buttonBGColor,
                  command=lambda: press("+"), height=buttonHeight, width=buttonWidth)
    plus.grid(row=5, column=3)

    minus = Button(gui, text=' - ', fg=buttonFGColor, bg=buttonBGColor,
                   command=lambda: press("-"), height=buttonHeight, width=buttonWidth)
    minus.grid(row=4, column=3)

    multiply = Button(gui, text=' * ', fg=buttonFGColor, bg=buttonBGColor,
                      command=lambda: press("*"), height=buttonHeight, width=buttonWidth)
    multiply.grid(row=3, column=3)

    divide = Button(gui, text=' / ', fg=buttonFGColor, bg=buttonBGColor,
                    command=lambda: press("/"), height=buttonHeight, width=buttonWidth)
    divide.grid(row=2, column=3)

    equal = Button(gui, text=' = ', fg=buttonFGColor, bg=buttonBGColor,
                   command=equalpress, height=buttonHeight, width=buttonWidth)
    equal.grid(row=6, column=3)

    clear = Button(gui, text='C', fg=buttonFGColor, bg=buttonBGColor,
                   command=clear, height=buttonHeight, width=buttonWidth)
    clear.grid(row=1, column=2)

    Decimal = Button(gui, text='.', fg=buttonFGColor, bg=buttonBGColor,
                     command=lambda: press('.'), height=buttonHeight, width=buttonWidth)
    Decimal.grid(row=6, column=2)

    Modulo = Button(gui, text='%', fg=buttonFGColor, bg=buttonBGColor,
                    command=lambda: press('%'), height=buttonHeight, width=buttonWidth)
    Modulo.grid(row=2, column=2)

    Sqrt = Button(gui, text='sqrt', fg=buttonFGColor, bg=buttonBGColor,
                  command=lambda: press('math.sqrt'), height=buttonHeight, width=buttonWidth)
    Sqrt.grid(row=6, column=0)

    power = Button(gui, text='**', fg=buttonFGColor, bg=buttonBGColor,
                   command=lambda: press('**'), height=buttonHeight, width=buttonWidth)
    power.grid(row=1, column=3)

    parenthesesOpen = Button(gui, text='(', fg=buttonFGColor, bg=buttonBGColor,
                             command=lambda: press('('), height=buttonHeight, width=buttonWidth)
    parenthesesOpen.grid(row=2, column=0)

    parenthesesClose = Button(gui, text=')', fg=buttonFGColor, bg=buttonBGColor,
                              command=lambda: press(')'), height=buttonHeight, width=buttonWidth)
    parenthesesClose.grid(row=2, column=1)

    leftShift = Button(gui, text='<<', fg=buttonFGColor, bg=buttonBGColor,
                              command=lambda: press('<<'), height=buttonHeight, width=buttonWidth)
    leftShift.grid(row=1, column=0)

    rightShift = Button(gui, text='>>', fg=buttonFGColor, bg=buttonBGColor,
                              command=lambda: press('>>'), height=buttonHeight, width=buttonWidth)
    rightShift.grid(row=1, column=1)

    # start the GUI
    gui.mainloop()
