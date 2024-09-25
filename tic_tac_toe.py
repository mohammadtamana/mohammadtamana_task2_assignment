# Function to display the Tic Tac Toe board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full (draw)
def is_draw(board):
    return all([spot != " " for spot in board])

# Function to play the Tic Tac Toe game
def play_game():
    while True:
        # Initialize the board and player turn
        board = [" "] * 9
        current_player = "X"
        game_over = False

        print("Welcome to Tic Tac Toe!")
        display_board(board)

        # Game loop
        while not game_over:
            print(f"Player {current_player}'s turn.")
            
            # Handle input with validation
            try:
                move = int(input(f"Choose a position (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            # Update the board with the player's move
            board[move] = current_player
            display_board(board)

            # Check for a winner
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                game_over = True
            elif is_draw(board):
                print("It's a draw!")
                game_over = True
            else:
                # Switch players
                current_player = "O" if current_player == "X" else "X"

        # Ask to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()