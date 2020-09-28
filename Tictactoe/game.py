# Board 
# display board
# play game
# handle turn
# check win 
#     check rows
#     check columns
#     check diagonals
# check tie 
# flip player

# --------------- Global Variables ---------------------
flip = True
# Game Board hold data of the game
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Two player
X = "X"
O = "O"

#Start player
current_player = X

# Who won or tie?
winner = None

# Checking this game is playing or game over
game_still_ongoing = True

#Display a board game in the creen
def display_board():
    #display attractive position for player know the position of board in the creen
    position_display = ["       | 1 | 2 | 3 | ", "       | 4 | 5 | 6 | ", "       | 7 | 8 | 9 | "]
    # Display 3 value of board in 1 rows and additional view of these position
    for i in range(3):
        print(" | {0} | {1} | {2} | {3}".format(board[3*i], board[3*i + 1], board[3*i + 2], position_display[i])) 

#Executing a turn for a player
def handle_turn():
    #Set global variables
    global current_player
    # Print in the sreen who has this turn?
    print(current_player + "'s turn!!!")
    # Variable for checking input is valid format
    valid_input_position = False
    # Pisition player choose
    position = ""
    # Checking valid position and this position still None
    while(not valid_input_position):
        position = input("Choose a position from 1-9: ") 
        # check valid position input is a number from 1 - 9
        if position.isalnum() and position in "123456789":
            #Checking position still not fill
            if not board[int(position)-1] == "-":
                print("*Position has valued, Pic a gain")
            else: 
                valid_input_position = True
        else:
            print("*Not valid position input, Type a gain")
    
    #Update value for board
    board[int(position)-1] = current_player

    #Display board game 
    display_board()

# Change the turn for other player
def flip_player():
    global flip, current_player
    # flip = True for first player(X), and False for second player(O)
    if flip:
        # first player
        current_player = O
    else:
        # second player
        current_player = X

    #end turn/ change flip for next player
    flip = not flip


#Checking have a winner or no position available in the board(tie)
def check_game_over():
    global winner
    #Found the winner in this turn
    check_if_win()
    #The last turn but not found the winner
    check_if_tie()

def check_if_win():
    #Set global values
    global game_still_ongoing, winner
    # Get winner from row, column or diagnoals
    row_winner = winner_row()
    column_winner = winner_column()
    diagonals_winner = winner_diagonals()
    # if a row, column or a diagnol touch win rule -> set winner = current_player
    if row_winner or column_winner or diagonals_winner:
        winner = current_player
        game_still_ongoing = False

#Checking have a row with same value of current player
def winner_row():
    win = False
    for i in range(3):
        row_check = board[3*i] == board[3*i+1] == board[3*i+2] != "-"
        win = win or row_check
    return win

#Checking have a column with same value of current player
def winner_column():
    win = False
    for i in range(3):
        column_check = board[i] == board[i+3] == board[i+6] != "-"
        win = win or column_check
    return win

#Checking have a diagonal with same value of current player
def winner_diagonals():
    diagonal1 =  board[0] == board[4] == board[8] != "-"
    diagonal2 =  board[2] == board[4] == board[6] != "-"
    return diagonal1 or diagonal2

#Checking if the board game has no available position and game over with tie
def check_if_tie():
    global game_still_ongoing
    check_not_fill_position = "-" in board
    if not check_not_fill_position:
        game_still_ongoing = False

def play_game():

    #Initial the game 
    display_board()

    #game still in play
    while(game_still_ongoing):
        
        #handling a turn of a player
        handle_turn()

        #checking if the game has get stop case
        check_game_over()

        #if not over game will continue, so change turn for next player
        flip_player()

    #Executing for game over
    if winner == X or winner == O:
        print(winner + "  Won.")
    elif winner == None:
        print("Tie")