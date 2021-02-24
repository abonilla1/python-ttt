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
#Boolean to hold game status
game_not_over = True   
#winner
winner = None
#current move
current_player = "X"
#creates win patterns list to check conditions (will hold the board indeces/squares that need to be the same in order to be considered a win)
win_conditions = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

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
    check_win(board)
    # check_cat(board)
 
 #loop through the board, return the index of every o and x and compare them to win_conditions

def check_win(board):
    x_list = []
    o_list = []
    for square in range(9):
        if board[int(square)] == "X": 
           index = int(square) 
           x_list.append(index)
        elif board[int(square)] == "O":
           indexo = int(square)
           o_list.append(indexo)
        else:
            pass
    for win in win_conditions:
        if x_list.sort() == win:
            winner = "X"
            print(f"{winner} wins!")
            game_not_over = False
        elif o_list.sort() == win:
            winner = "O"
            print(f"{winner} wins!")
            game_not_over = False
        else:
            return


# def check_cat(board):
    #some logic here
    
 

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
    while game_not_over:
        handle_turn(current_player)
        check_if_game_over(board)
        current_player = handle_turn_change(current_player)
     
        

play(current_player)


