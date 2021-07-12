from tkinter import *
import tkinter.font as font

root = Tk()

insertField = Entry(root, width=45, borderwidth=5)
insertField.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady=10)


result = 0.0
action = "plus"
startPos = True
insertField.insert(0, "0")

def numButtonClick(num: int):
    global startPos
    if startPos:
        insertField.delete(0, END)
        startPos = False

    currentField = insertField.get()
    insertField.delete(0, END)
    insertField.insert(0, currentField + str(num))

def clearButtonClick():
    global action, startPos, result
    result = 0
    action = "plus"
    insertField.delete(0, END)
    insertField.insert(0, "0")
    startPos = True


def equalButtonClick():
    global action, startPos, result
    startPos = True

    if action == "plus":
        result += float(insertField.get())
    elif action == "minus":
        result -= float(insertField.get())
    elif action == "multiple":
        result *= float(insertField.get())
    elif action == "division":
        result /= float(insertField.get())
    
    action = "plus"

    insertField.delete(0, END)
    insertField.insert(0, str(result))
    result = 0

def notButtonClick():
    currentField = insertField.get()
    if len(currentField) <= 0 or (len(currentField) == 1 and currentField[0] == "0"):
        return
    insertField.delete(0, END)
    if currentField[0] == "-":
        insertField.insert(0, currentField[1:])
    else:
        insertField.insert(0, "-" + currentField)


def buttonClickOperation(operation):
    global result, action

    if action == "plus":
        result += float(insertField.get())
    elif action == "minus":
        result -= float(insertField.get())
    elif action == "multiple":
        result *= float(insertField.get())
    elif action == "division":
        result /= float(insertField.get())

    action = operation

    insertField.delete(0, END)


# Define buttons

calcButton9 = Button(root, text="9", padx=40, pady=20, command=lambda: numButtonClick(9))
calcButton8 = Button(root, text="8", padx=40, pady=20, command=lambda: numButtonClick(8))
calcButton7 = Button(root, text="7", padx=40, pady=20, command=lambda: numButtonClick(7))
calcButton6 = Button(root, text="6", padx=40, pady=20, command=lambda: numButtonClick(6))
calcButton5 = Button(root, text="5", padx=40, pady=20, command=lambda: numButtonClick(5))
calcButton4 = Button(root, text="4", padx=40, pady=20, command=lambda: numButtonClick(4))
calcButton3 = Button(root, text="3", padx=40, pady=20, command=lambda: numButtonClick(3))
calcButton2 = Button(root, text="2", padx=40, pady=20, command=lambda: numButtonClick(2))
calcButton1 = Button(root, text="1", padx=40, pady=20, command=lambda: numButtonClick(1))
calcButton0 = Button(root, text="0", padx=40, pady=20, command=lambda: numButtonClick(0))
calcButtonPlus = Button(root, text="+", padx=40, pady=20, command=lambda: buttonClickOperation("plus"))
calcButtonMinus = Button(root, text="-", padx=40, pady=20, command=lambda: buttonClickOperation("minus"))
calcButtonEqual = Button(root, text="=", padx=40, pady=20, command=equalButtonClick)
calcButtonMult = Button(root, text="*", padx=40, pady=20, command=lambda: buttonClickOperation("multiple"))
calcButtonDiv = Button(root, text="/", padx=40, pady=20, command=lambda: buttonClickOperation("division"))
calcButtonNot = Button(root, text="+/-", padx=40, pady=20, command=notButtonClick)
calcButtonClear = Button(root, text="CLEAR", padx=10, pady=5, command=clearButtonClick)

# Hold buttons on the screen

calcButton9.grid(row=1, column=2)
calcButton8.grid(row=1, column=1)
calcButton7.grid(row=1, column=0)
calcButton6.grid(row=2, column=2)
calcButton5.grid(row=2, column=1)
calcButton4.grid(row=2, column=0)
calcButton3.grid(row=3, column=2)
calcButton2.grid(row=3, column=1)
calcButton1.grid(row=3, column=0)
calcButton0.grid(row=4, column=1)
calcButtonPlus.grid(row=4, column=3)
calcButtonMinus.grid(row=3, column=3)
calcButtonEqual.grid(row=4, column=2)
calcButtonMult.grid(row=2, column=3)
calcButtonDiv.grid(row=1, column=3)
calcButtonNot.grid(row=4, column=0)
calcButtonClear.grid(row=0, column=3)

root.mainloop()