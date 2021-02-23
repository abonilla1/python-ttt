#====================================Minimal Game Logic=============================#
# I need:
# A board and a state of the game which will be controlled by the board
# Board needs to be displayed
# Player objects or variables, which will have turns and names of  'X' or 'O'
# A way to check the state of the game
    # check for win, tie scenarios
# A way to handle turns (check which turn it is)
#===================================================================================#



#====Board=====#

#creates board variable as a list of 9 items 
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  

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

#----turns-----#

next_turn = 'X'
def handle_turn():
    square = input("Enter a number between 1 and 9 to make your move: ")
    board[(int(square)-1)] = next_turn
    display()



#---main function---#
def play():
    print()
    print(f"{next_turn} goes first")
    display() #display the  initial board
    handle_turn()
    

play()
