# Goal: Create a Tic Tac Toe game in Python where two players can play against each other.
# Instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.

# Step 1: Representing the Game Board
# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).

board = [[' ', ' ', ' ' ],
         [' ', ' ', ' ' ],
         [' ', ' ', ' ' ]
]

#dictionary for user_input and indexes
board_dict = {(1, 1): (0, 0),
              (1, 2): (0, 1),
              (1, 3): (0, 2),
              (2, 1): (1, 0),
              (2, 2): (1, 1),
              (2, 3): (1, 2),
              (3, 1): (2, 0),
              (3, 2): (2, 1),
              (3, 3): (2, 2)}

#print(board_dict[(1,3)])


# Step 2: Displaying the Game Board
# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.

def display_board(board):
    print ('*' * 17)
    print (f'*   {board[0][0]} | {board[0][1]} | {board[0][2]}   *')
    print ('*  ---|---|---  *')
    print (f'*   {board[1][0]} | {board[1][1]} | {board[1][2]}   *')
    print ('*  ---|---|---  *')
    print (f'*   {board[2][0]} | {board[2][1]} | {board[2][2]}   *')
    print ('*' * 17)

#display_board(board)

# Step 3: Getting Player Input
# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.

def player_input (player):
    while True:
        display_board(board)
        print (f'Player\'s {player}\'s turn.')
        user_raw = int(input('Type a number of raw from 1 to 3: '))
        user_column = int(input('Type a number of column from 1 to 3: '))
        if (user_raw, user_column) in board_dict:
            i, j = board_dict[(user_raw, user_column)]
            if board[i][j] == ' ':
                board[i][j] = player
                break
    
#player_input(player='O')
    
    
# Step 4: Checking for a Winner
# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

winning_position = (#rows
                    [(0,0), (0,1), (0,2)],
                    [(1,0), (1,1), (1,2)],
                    [(2,0), (2,1), (2,2)],

                    #columns
                    [(0,0), (1,0), (2,0)],
                    [(0,1), (1,1), (2,1)],
                    [(0,2), (1,2), (2,2)],

                    #diagonals
                    [(0,0), (1,1), (2,2)],
                    [(0,2), (1,1), (2,0)],
     )

def check_win (board, player):
    
    for position in winning_position:
        Winner = True
        for i,j in position:
            if board[i][j] != player:
              Winner = False
              break
        if Winner:
            return True
    return False
         
# Step 5: Checking for a Tie
# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.

def checking_for_a_tie(board, player, check_win):
 
    if check_win(board,player):
        return False
    for i in range(3):
        for j in range(3):   
            if board[i][j] == ' ':
                return False
    return True

# Step 6: The Main Game Loop
# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

def play():
    global board
    board = [[' ', ' ', ' ' ],
            [' ', ' ', ' ' ],
            [' ', ' ', ' ' ]
    ]

    # #dictionary for user_input and indexes
    # board_dict = {(1, 1): (0, 0),
    #             (1, 2): (0, 1),
    #             (1, 3): (0, 2),
    #             (2, 1): (1, 0),
    #             (2, 2): (1, 1),
    #             (2, 3): (1, 2),
    #             (3, 1): (2, 0),
    #             (3, 2): (2, 1),
    #             (3, 3): (2, 2)}

    player = input("Choose your character (X or O): ")

    while True:
    
        player_input(player)

        if check_win (board, player):
            display_board(board)
            print(f'{player} wins!')
            break
        
        if checking_for_a_tie(board, player,check_win):
            display_board(board)
            print('There is a Tie')
            break
    
        player = 'O'if player == 'X' else 'X'  

play()  


# Tips:
# Consider creating helper functions to break down the logic into smaller, manageable parts.
# Follow the single responsibility principle: each function should do one thing and do it well.
# Think about how to switch between players.
# Think about how you will store the player’s symbol.
