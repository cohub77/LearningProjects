from array import *
from tkinter import *



def checkWin(arr):
    win = False
    # check rows
    for row in arr:
        if row[0] == row[1] == row[2] and row[0] is not None:
            win = True
    # check columns
    for col in range(3):
        if arr[0][col] == arr[1][col] == arr[2][col] and arr[0][col] is not None:
            win = True
    # check diagonals
    if arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0] is not None:
        win = True
    if arr[0][2] == arr[1][1] == arr[2][0] and arr[0][2] is not None:
        win = True
    return win

def spot(term):
    match term:
        case "1":
            place(0,0,y) 
        case "2":
            place(0,1,y) 
        case "3":
            place(0,2,y)
        case "4":
            place(1,0,y)
        case "5":
            place(1,1,y)
        case "6":
            place(1,2,y)
        case "7":
            place(2,0,y)
        case "8":
            place(2,1,y)
        case "9":
            place(2,2,y)
            
def place(loc, loc2, arr):
    global p
    if arr[loc][loc2] is not None:
        print("This space is already taken. Please choose another one.")
    else:
        if p == True:
            print(loc)
            arr[loc][loc2] = "X"
        else:
            arr[loc][loc2] = "O"
        if (checkWin(y) == False ):
            p = not p
        else:
            print("WWWWWWWWWWWW")

3
def turn():
    global p
    if (checkWin(y) == False ):
        t = " "
        if p:
            t = "Player 1 Turn"
        else: 
            t = "Player 2 Turn"
        z = input(t)
        spot(z)
        for r in y:
            for c in r:
                if c is not None:
                    print(c,end = " ")
                else:
                    print ("-",end = " ")
            print()
root = Tk()

def on_click(i,j):
    global p
    if y[i][j] is not None:
        print("This space is already taken. Please choose another one.")
    else:
        if p == True:
            y[i][j] = "X"
            buttons[i][j].config(text="X")
        else:
            y[i][j] = "O"
            buttons[i][j].config(text="O")
        if checkWin(y):
            if p:
                winner = "Player 1"
            else:
                winner = "Player 2"
            label.config(text=winner + " wins!")
        else:
            p = not p

p = True
y = [[None, None, None], [None, None, None], [None, None, None]]
buttons = [[None, None, None], [None, None, None], [None, None, None]]

label = Label(root, text=" ")
label.grid(row=3,column=0,columnspan=3)

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(root, text=" ", width=10, height=5, command=lambda i=i,j=j: on_click(i,j))
        buttons[i][j].grid(row=i,column=j)

root.mainloop()   
#while (checkWin(y) == False):
 #   turn()



