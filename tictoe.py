def print_board(board):
    """Prints the current state of the board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board, player):
    """Checks all 8 possible winning combinations."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    """Checks if there are any empty spaces left."""
    return ' ' not in board

def play_game():
    """Main game loop."""
    # Initialize an empty board with 9 spaces
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Command-Line Tic-Tac-Toe!")
    print("Positions are numbered 1-9, starting from the top left:")
    # Print a guide board to show players which number corresponds to which square
    print_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose your move (1-9): ")

        # 1. Validate the input (must be a number between 1 and 9)
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("⚠️ Invalid input. Please enter a number between 1 and 9.")
            continue

        move_index = int(move) - 1

        # 2. Check if the spot is already taken
        if board[move_index] != ' ':
            print("⚠️ That spot is already taken! Try again.")
            continue

        # 3. Apply the move to the board
        board[move_index] = current_player

        # 4. Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! Congratulations!")
            break

        # 5. Check for a tie
        if is_board_full(board):
            print_board(board)
            print("🤝 It's a tie! Well played both.")
            break

        # 6. Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
