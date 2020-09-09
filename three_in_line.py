from random import randrange

def displayBoard(board):
    print()
    print(("+--------"),("+--------"),("+--------"), '+', sep="")
    print(("|        "),("|        "),("|        "), '|', sep="")
    print((f"|    {board[0][0]}   "),(f"|    {board[0][1]}   "),(f"|    {board[0][2]}   "), '|', sep="")
    print(("|        "),("|        "),("|        "), '|', sep="")
    print(("+--------"),("+--------"),("+--------"), '+', sep="")
    print(("|        "),("|        "),("|        "), '|', sep="")
    print((f"|    {board[1][0]}   "),(f"|    {board[1][1]}   "),(f"|    {board[1][2]}   "), '|', sep="")
    print(("|        "),("|        "),("|        "), '|', sep="")
    print(("+--------"),("+--------"),("+--------"), '+', sep="")
    print(("|        "),("|        "),("|        "), '|', sep="")
    print((f"|    {board[2][0]}   "),(f"|    {board[2][1]}   "),(f"|    {board[2][2]}   "), '|', sep="")
    print(("|        "),("|        "),("|        "), '|', sep="")
    print(("+--------"),("+--------"),("+--------"), '+', sep="")

def enterMove(board):
    choice= True

    # maybe not a good practice but just as a remainder that
    # you can rearrange dynamically the type of your variables in Python
    
    while choice:
        try:            
            choice= input("\nPlease, enter your move as an integer: ")
            choice= int(choice)     
            break
        except:
            print("It should be written as an integer...")

    return choice


def makeListOfFreeFields(board):
    
    di= dict()
    counter= 0
    keys=[]
    options= list() 
    possibilities= list()
    
    for i in range(3):      # creates a dictionary with the values of the list board
        for j in range(3):
            di[counter]= (i,j)
            counter +=1
            
    keys= di.keys()
    for i in range(3):
        for j in range(3):
            for k in keys:
                if k+1 == board[i][j]:
                    options.append(k)
                else:
                    continue
    if moves%2 ==0:            
        print("These are the positions available:\n ")
        for i in options:
            for k,v in di.items():
                if i == k:
                    print(i+1, v, sep="-> ")

    return options
        

def victoryFor(board):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    if moves > 4 and moves <= 10:
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2])\
                or (board[0][i] == board[1][i] == board[2][i])\
                or (board[0][0] == board[1][1] == board[2][2])\
                or (board[0][2] == board[1][1] == board[2][0]):
                        if moves%2 == 0: # It has been changed in updateBoard()
                            print("\n#### The winner is the machine ####")
                            return True
                        else:
                            print("\n#### You won! ####")
                            return True
        else:
            if moves==10:
                print("\n#### This is a tie! ####")
                return True
            else:
                return False
    else:
        return False
        
        

def drawMove(options):
#
# the function draws the computer's move and updates the board
#

    pool= 0
    choice= 0
    num= 0
    
    if moves== 1:
        choice= 5
    else:
        pool= len(options)
        num= randrange(pool)
        choice= options[num] +1  # options starts at 0 and board at 1 so it can be confusing
    
    return choice
    

def turnPlayer(board):
    victory= False
    options=[]
    
    while not victory:
        options= makeListOfFreeFields(board)
           
        if moves%2 != 0: 
            choice = drawMove(options)
            board= updateBoard(choice)
        else:
            displayBoard(board)
            choice= enterMove(options)
            board= updateBoard(choice)
            
        victory= victoryFor(board)

    displayBoard(board)
    print("\nThanks for playing!")
        
        
def createBoard():
    # creates the board as a 3x3 list

    for i in range(3):
        if i == 0:
            row=[]
            for j in range(1,4):
                row.append(j)
            board.append(row)
        elif i == 1:
            row=[]
            for k in range(4,7):
                row.append(k)
            board.append(row)
        else:
            row=[]
            for l in range(7,10):
                row.append(l)
            board.append(row)
            
    displayBoard(board)
                
    return board


def updateBoard(choice):
    global board, moves

    for i in range(3):
        for j in range(3):
            if choice == board[i][j]:
                if moves%2 != 0:
                    board[i][j]= 'X'
                    moves += 1
                else:
                    board[i][j]= 'O'
                    moves += 1
            else:
                continue

    return board
          

# start program

board=[]
moves= 1


board= createBoard()
turnPlayer(board)


