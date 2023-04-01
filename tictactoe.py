from array import *
p = True
y = [[None, None, None], [None, None, None], [None, None, None]]

def checkWin(arr):
    win = False
    if (arr[0][0] == arr[0][1] == arr[0][2] and arr[0][0] is not None):
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
    if p == True:
        print(loc)
        arr[loc][loc2] = "X"
    else:
        arr[loc][loc2] = "O"
    if (checkWin(y) == False ):
        p = not p
    else:
        print("WWWWWWWWWWWW")

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
    
while (checkWin(y) == False):
    turn()



