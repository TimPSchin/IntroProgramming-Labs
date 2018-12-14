#CMPT 120 Intro to PRogramming
#Lab #7
#Timothy Schindler
#Created: 11/8/18

symbol = [" ", "x", "o"]
def printRow(row):
    output = "|"
    for cell in row:
        output += " " + symbol[cell] + " |"
    print(output)
   
def printBoard(board):
    print("+-----------+")
    for row in board: # row will contain a list, which represent a single row of the board
        printRow(row)
        print("+-----------+")
    

def markBoard(board, row, col, player):
    #check to see wheher the desired square is blank
        #if so, set it to the player number
    pass

def getPlayerMove():
    input("")#prompt the user separately for the row and colum number
    return(0,0)#then return that row and column instead of (0,0)

def hasBlanks(board):
    #for each row in the board..
        #for each square in the row..
            #check whether the square is blank
                #if so, return true
    return True #if no square is blank, return False

def main():
    board = [ [0,0,0], [0,0,0], [0,0,0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1
main()
