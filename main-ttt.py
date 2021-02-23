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

def check_if_game_over():
    check_win()
    check_tie()

def check_win():

def check_tie():   

#----turns-----#


def handle_turn(current_player):
    square = input("Enter a number between 1 and 9 to make your move: ")
    board[(int(square)-1)] = current_player
    display()

def handle_turn_change():

#---main function---#


def play():
    print()
    display() #display the initial board
    while game_not_over:
        handle_turn(current_player)

        check_if_game_over()

        handle_turn_change()
    
    if winner != None:
        print(f"{winner} Won!")
    else:
        print("Tie game")    
        

play()


