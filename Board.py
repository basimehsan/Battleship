import random

class Board:
    
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.arr = [['W' for a in range(self.rows)]for b in range(self.cols)]
        self.setBoard()    

    def setBoard(self):
        self.sethorizonatalship()
        self.setverticalship()
        self.setverticalship()
        self.setverticalship()
        self.sethorizonatalship()

    def sethorizonatalship(self):
        while True:
            xcor = random.randint(0,9)
            ycor = random.randint(0,9)
            #print("Horizontal: " + str(xcor) + '\t' + str(ycor))
            if int(xcor) < 8 and int(ycor) < 8 and str(self.arr[int(xcor)][int(ycor)])== 'W' and str(self.arr[int(xcor)][int(ycor)+1]) == 'W' and str(self.arr[int(xcor)][int(ycor)+2]) == 'W':
                break
        self.arr[int(xcor)][int(ycor)] = 'S'
        self.arr[int(xcor)][int(ycor)+1] = 'S'
        self.arr[int(xcor)][int(ycor)+2] = 'S'

    def setverticalship(self):
        while True:
            xcor = random.randint(0,9)
            ycor = random.randint(0,9)
            #print("Vertical: " + str(xcor) + '\t' + str(ycor))
            if int(xcor) < 8 and int(ycor) < 8 and str(self.arr[int(xcor)][int(ycor)]) == 'W' and str(self.arr[int(xcor)+1][int(ycor)]) == 'W' and str(self.arr[int(xcor)+2][int(ycor)]) == 'W':
                break
        self.arr[int(xcor)][int(ycor)] = 'S'
        self.arr[int(xcor)+1][int(ycor)] = 'S'
        self.arr[int(xcor)+2][int(ycor)] = 'S'

    def showBoard(self):
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
                print(str(self.arr[a][b]) + '\t', end= '')
            print('\n')