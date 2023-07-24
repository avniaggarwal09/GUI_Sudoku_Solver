from tkinter import *
from solver import solver

root = Tk()
root.title("Sudoku Solver")
root.geometry("324x550")

label = Label(root, text="Fill in the numbers and click solve ").grid(row=0, column=1, columnspan=10)

# incorrect answer/ game unsolved
errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)

# correct answer/ game solved
solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

# empty dictionary to store each cell of input grid
cells = {}

"""will control what is being entered into the cells
and will take value of cell as an argument"""
def ValidateNumber(P):
    out = (P.isdigit() or P == "") and len(P)<2
    return out

# to register the function to the window
reg = root.register(ValidateNumber)

# function to draw 3x3 grid
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            """
            justify = center to center align the text
            validate = key to call the validate function upon keypress
            validatecommand = tuple of reg fxn and %P substitution code
                to pass new value to fxn on change"""
            e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row+i+1, column=column+j+1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = e

# function to draw 9x9 grid
def draw9x9Grid():
    color="#D0ffff"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"

# function to clear values in each cell
def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")

# function to get values
def getValues():
    # empty list where we will store the values for each cell
    board=[]
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        rows=[]     # empty list for each row
        for col in range(1, 10):
            # get the value of cell using entry widget get method
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        # append rows list to board list
        board.append(rows)
    updateValues(board)

# creation of button using button widget
btn = Button(root, command=getValues, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

btn = Button(root, command=clearValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)

# function to update the cells and display the solution of sudoku
def updateValues(s):
    sol=solver(s)
    if sol!="No":
        for rows in range(2,11):
            for cols in range(1,10):
                cells[(rows, cols)].delete(0,"end")
                cells[(rows, cols)].insert(0, sol[rows-2][cols-1])
        # to set text of solvedLabel to sudoku solved using configure method
        solvedLabel.configure(text="Sudoku solved! ")
    else:
        errLabel.configure(text="No solution exists for this sudoku")

# call 9draw9x9Grid function and roots main loop method to launch the instance of created window
draw9x9Grid()
root.mainloop()