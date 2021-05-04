import random
import math
from Board import Board

playerHitCount = 0 
computerHitCount = 0

def coltoint(y):  #converts column letter to column number
    global yint
    yint = 0
    if str(y) == 'A':
        yint = 0
    elif str(y) == 'B':
        yint = 1
    elif str(y) == 'C':
        yint = 2
    elif str(y) == 'D':
        yint = 3
    elif str(y) == 'E':
        yint = 4
    elif str(y) == 'F':
        yint = 5
    elif str(y) == 'G':
        yint = 6
    elif str(y) == 'H':
        yint = 7
    elif str(y) == 'I':
        yint = 8
    elif str(y) == 'J':
        yint = 9
    
def inttocol(ycor):  #Converts column number to column letter
    global ycor_str
    ycor_str = ':O'
    if int(ycor) == 0:
        ycor_str = 'A'
    elif int(ycor) == 1:
        ycor_str = 'B'
    elif int(ycor) == 2:
        ycor_str = 'C'
    elif int(ycor) == 3:
        ycor_str = 'D'
    elif int(ycor) == 4:
        ycor_str = 'E'
    elif int(ycor) == 5:
        ycor_str = 'F'
    elif int(ycor) == 6:
        ycor_str = 'G'
    elif int(ycor) == 7:
        ycor_str = 'H'
    elif int(ycor) == 8:
        ycor_str = 'I'
    elif int(ycor) == 9:
        ycor_str = 'J'

def instructions():
    print("\n                       Hi! Let's play BATTLESHIP!                        \n")
    print("                       Let's have a look at your ships\n")
    player.showBoard()
    print("\n Your opponent shares a similar board but you don't know where their ships are yet!\n")
    print("Here is some information you might need:\nU: Unknown\nW: Water\nS: Ship\nX: Destroyed Ship")
    print("\nThere are a total of 5 ships that each you and your opponent own. Whoever destroys \nall of the others' ships first wins.")
    print("\nPress enter to proceed")
    input()
    print("Guess the location of your opponent's ship to play against the computer")

def gameplay():
    while True:
        print("\nRow: ", end = '')
        x = input()
        if x == '':
            print("Please, type an integer in the range 1-10")
            continue
        x=int(x)
        x-=1
        print("Column: ", end = '')
        y = input()

        if (int(x) < 0 or int(x) > 9) or (str(y) != 'A' and str(y) != 'B' and str(y) != 'C' and str(y) != 'D' and str(y) != 'E' and str(y) != 'F' and str(y) != 'G' and str(y) != 'H' and str(y) != 'I' and str(y) != 'J'):
            print("Invalid Input. Row should be in the range 1-10 and Column should be a capital letter\nfrom A to J.\n")
            continue 

        print("")
        coltoint(str(y))

        if guess_arr[int(x)][int(yint)] == "X":
            print("Already Hit Before")
            continue
        
        if guess_arr[int(x)][int(yint)] == "W":
            print("#$@&%*! Here's water. You hit here before")
            continue
       
        player_guess(int(x),int(yint))

        if input("Press enter to let the computer make a guess or -1 to exit the game\n") == '-1':
            print("Bye!")
            exit()
        computer_guess()

        if int(playerHitCount) == 15:
            print("CONGRATULATIONS!!!!!!! YOU WON!!!!")
            exit()
        elif int(computerHitCount) == 15:
            print("Seems like the computer won. Better luck next time.")
            exit()
        elif int(playerHitCount) < 15 or int(computerHitCount) < 15:
            print("You have " +  str(math.floor((15-playerHitCount)/3)) + " ships and " + str((15-playerHitCount)%3) + "/3 of a ship left\n")
            print("Computer has " +  str(math.floor((15-computerHitCount)/3)) + " ships and " + str((15-computerHitCount)%3) +"/3 of a ship left\n")


def player_guess(xcor, ycor):
    global playerHitCount
    if str(computer.arr[int(xcor)][int(ycor)]) == 'S':
        guess_arr[int(xcor)][int(ycor)] = 'X'
        printBoard(guess_arr)
        print("                              YOU HIT A SHIP YAYY! :))\n")
        playerHitCount+=1
    else:
        guess_arr[int(xcor)][int(ycor)] = 'W'
        printBoard(guess_arr)
        print('                                 MISS!  :((                                     \n')
        print("                   Dude, What are you doing??? That's water     \n")
        print("                         Please, don't waste ammunition!        \n")
        

def computer_guess():
    global computerHitCount

    while True:
        xcor = random.randint(0,9) #row
        ycor = random.randint(0,9) #column
        if comp_guess_arr[int(xcor)][int(ycor)] == 'U':
            break
        
    inttocol(int(ycor))
    print("Row: "+ str(xcor+1))
    print("Column: " + str(ycor_str) + '\n')
    if str(player.arr[int(xcor)][int(ycor)]) == 'S':
        player.arr[int(xcor)][int(ycor)] = 'X'
        comp_guess_arr[int(xcor)][int(ycor)] = 'X'
        player.showBoard()
        print("                      Computer made a HIT!!! :((\n                                        ")
        computerHitCount+=1
    else:
        comp_guess_arr[int(xcor)][int(ycor)] = 'W'
        player.showBoard()
        print('                      Computer missed your ship!!! :))\n                                   ')

def printBoard(arr):
        rows = 10
        cols = 10
        colNames = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        for z in colNames:
            print(str(z) + '\t', end= '')
        print('\n')

        rowcount = 1
        for a in range(rows):
            print(str(rowcount) + '\t', end='')
            rowcount+=1
            for b in range(cols):
                print(str(arr[a][b]) + '\t', end= '')
            print('\n')



guess_arr = [['U' for a in range(10)]for b in range(10)]
comp_guess_arr = [['U' for a in range(10)]for b in range(10)]

if __name__ == "__main__":

    computer = Board()
    #computer.showBoard()

    player = Board()
    instructions()
    gameplay()
    
