#====================================Minimal Game Logic=============================#
# I need:
# A board and a state of the game which will be controlled by the board
# Board needs to be displayed
# Player objects or variables, which will have turns and names of  'X' or 'O'
# A way to check the state of the game
    # check for win, tie scenarios
# A way to handle turns (check which turn it is)
#===================================================================================#

#======Globals=======#

#creates board variable as a list of 9 items 
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] 
init_board =  ["1", "2", "3", "4", "5", "6", "7", "8", "9"] 
#current move
current_player = "X"
#creates win patterns list to check conditions (will hold the board indeces/squares that need to be the same in order to be considered a win)


#====Board=====#
#creates function to display board
def display():
    print()   #adds an empty line for visibility
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("=========")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("=========")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

#====State=====#

def check_if_game_over(board):
    status = check_win(board)
    if not any(filter(lambda x: x in init_board, board)):
        if status == True:
            print("Cat's game")
            return False
    else:
        return status
   

def check_win(board):
    if board[0] == board[1] == board[2]:
        if board[0] == "X":
            print("X wins!")
            return False
        else:
            print("O wins!")
            return False
    elif board[3] == board[4] == board[5]:
        if board[3] == "X":
            print("X wins!")
            return False
        else:
            print("O wins!")
            return False
    elif board[6] == board[7] == board[8]:
        if board[6] == "X":
            print("X wins!")
            return False
        else:
            print("O wins!")
            return False
    elif board[0] == board[3] == board[6]: 
        if board[6] == "X":
            print("X wins!")
            return False
        else:
            print("O wins!")
            return False
    elif board[1] == board[4] == board[7]:
        if board[1] == "X":
            print("X wins!")
            return False
        else:
            print("O wins!")
            return False      
    elif board[2] == board[5] == board[8]:
        if board[2] == "X":
            print("X wins!")
            return False
        else:
            print("O wins!")
            return False   
    elif board[0] == board[4] == board[8]:
        if board[0] == "X":
            print("X wins!")
            return False
        else:
            print("O wins!")
            return False
    elif board[2] == board[4] == board[6]:
        if board[6] == "X":
            print("X wins!")
            return False
        else:
            print("O wins!")
            return False
    else:
        return True
                
#----turns-----#

#A very simple turn change function that uses one conditional to change the string

def handle_turn(current_player):
    square = input("Enter a number between 1 and 9 to make your move: ") #get user input
    board[(int(square)-1)] = current_player #update board
    display() #display updated board

def handle_turn_change(current_player):
    if current_player == "X":
        current_player = "O"
        print(f"{current_player}'s turn!")
        print()
        return current_player
    else:
        current_player = "X"  
        print(f"{current_player}'s turn!")
        print()
        return current_player

#---main function---#


def play(current_player):
    print()
    display() #display the initial board
    print()
    game_not_over = True 
    while game_not_over:
        handle_turn(current_player)
        game_not_over = check_if_game_over(board)
        if game_not_over:
            current_player = handle_turn_change(current_player)
        else:
            pass

play(current_player)


