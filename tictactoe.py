"""
Improved Procedural Tic Tac Toe (Console Version)

Key features:
- Purely procedural design
- Clear separation of concerns using functions
- Input validation
- Refactored logic into small, readable functions
- Suitable for explaining algorithms in an academic assignment
"""

# -----------------------------
# CONSTANTS AND GLOBAL SETTINGS
# -----------------------------

# All possible winning lines on a 3x3 Tic Tac Toe board.
# Each tuple stores the indices in the board list that form a winning line.
WINNING_LINES = [
    (0, 1, 2),  # Top row
    (3, 4, 5),  # Middle row
    (6, 7, 8),  # Bottom row
    (0, 3, 6),  # Left column
    (1, 4, 7),  # Middle column
    (2, 5, 8),  # Right column
    (0, 4, 8),  # Top-left to bottom-right diagonal
    (2, 4, 6)   # Top-right to bottom-left diagonal
]


# -----------------------------
# BOARD CREATION AND DISPLAY
# -----------------------------

def create_board():
    """
    Create and return a new empty Tic Tac Toe board.

    The board is represented as a list of 9 strings.
    Each element is either:
    - " " (space) for empty, or
    - "X" / "O" for player moves.

    Using a list with 9 elements is simple and easy to index.
    """
    return [" "] * 9


def display_board(board):
    """
    Print the current state of the board in a 3x3 grid.

    Index mapping for user understanding:
        1 | 2 | 3
       ---+---+---
        4 | 5 | 6
       ---+---+---
        7 | 8 | 9

    The board list uses indices 0–8, so we map them visually.
    """
    print()  # Empty line for spacing
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()  # Empty line for spacing


# -----------------------------
# INPUT VALIDATION FUNCTIONS
# -----------------------------

def is_valid_position(position_str):
    """
    Validate the raw user input for a move.

    Steps:
    1. Check that the input is numeric (e.g., "1", "2", ..., "9").
    2. Convert to an integer.
    3. Check that the integer is in the range 1–9.
    4. Convert to a board index (0–8) if valid.

    Returns:
        (True, index) if the input is valid.
        (False, None) if the input is invalid.
    """
    # First, ensure the input is made of digits only.
    if not position_str.isdigit():
        return False, None

    # Convert string to integer.
    position = int(position_str)

    # Check that the input is between 1 and 9.
    if 1 <= position <= 9:
        # Subtract 1 to convert to a 0-based index for the board list.
        return True, position - 1

    # Anything outside 1–9 is invalid.
    return False, None


def is_empty_square(board, index):
    """
    Check if a given board position is empty.

    Arguments:
        board: the current game board list.
        index: the position to check (0–8).

    Returns:
        True if the square is empty (contains " "), False otherwise.
    """
    return board[index] == " "


# -----------------------------
# CORE GAME LOGIC FUNCTIONS
# -----------------------------

def make_move(board, index, player):
    """
    Place the player's symbol on the board at the given index.

    This function directly updates the board list.

    Arguments:
        board: the current board list.
        index: the position to place the symbol (0–8).
        player: the current player ("X" or "O").
    """
    board[index] = player


def check_winner(board, player):
    """
    Check if the given player has won the game.

    The function loops through all predefined WINNING_LINES.
    For each line (a, b, c), it checks if all 3 squares on the board
    contain the player's symbol.

    Complexity:
        The number of winning lines is fixed (8), so this is O(1).

    Returns:
        True if the player has a winning line, False otherwise.
    """
    for a, b, c in WINNING_LINES:
        # Check that all three positions in the line match the player's symbol.
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw(board):
    """
    Check if the game is a draw.

    A draw happens when:
    - All squares are filled (no spaces left), and
    - No player has won.

    This function only checks if there are no spaces left.
    It is usually called AFTER checking for a winner.

    Returns:
        True if the board has no empty squares, False otherwise.
    """
    return " " not in board


def switch_player(current_player):
    """
    Switch the active player.

    If the current player is "X", return "O".
    If the current player is "O", return "X".

    This keeps the code simple and avoids repetition.

    Returns:
        The new current player symbol ("X" or "O").
    """
    return "O" if current_player == "X" else "X"


# -----------------------------
# USER INPUT WRAPPER
# -----------------------------

def get_player_move(board, player):
    """
    Ask the current player to choose a move and return a valid index.

    This function handles:
    - Asking for input.
    - Validating the input (correct type and range).
    - Ensuring the chosen square is empty.

    It uses a loop that continues until the player provides a valid move.
    This protects the game from invalid or malicious input.

    Returns:
        A valid index (0–8) where the move can be made.
    """
    while True:
        # Ask the player for a move and strip extra spaces.
        raw = input(f"Player {player}, choose a square (1–9): ").strip()

        # Validate the input string (e.g., "1"–"9").
        valid, index = is_valid_position(raw)
        if not valid:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue  # Ask again if invalid.

        # Check that the chosen square is not already taken.
        if not is_empty_square(board, index):
            print("That square is already taken. Please choose another one.")
            continue  # Ask again if square is occupied.

        # If we get here, the move is valid and the square is empty.
        return index


# -----------------------------
# MAIN GAME LOOP FUNCTIONS
# -----------------------------

def play_single_game():
    """
    Run one full game of Tic Tac Toe.

    Steps:
    1. Create a new empty board.
    2. Set current_player to "X".
    3. Repeatedly:
       - Display the board.
       - Ask the current player for a valid move.
       - Make the move.
       - Check if that player has won.
       - Check if the game is a draw.
       - Switch players if the game continues.

    The function exits once there is a winner or a draw.
    """
    # Start with a fresh board.
    board = create_board()

    # X always starts first.
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Player X goes first.")
    display_board(board)

    # Main game loop.
    while True:
        # Get a valid move from the current player.
        move_index = get_player_move(board, current_player)

        # Apply the move to the board.
        make_move(board, move_index, current_player)

        # Show the updated board.
        display_board(board)

        # Check if this move caused the current player to win.
        if check_winner(board, current_player):
            print(f"Player {current_player} wins! 🎉")
            break  # End the game loop if we have a winner.

        # If no winner, check if the game is a draw.
        if is_draw(board):
            print("It's a draw! 🤝")
            break  # End the game loop if the board is full.

        # Swap to the other player and continue.
        current_player = switch_player(current_player)


def ask_play_again():
    """
    Ask the user if they want to play another game.

    The function keeps asking until the user provides a clear 'yes' or 'no'.
    This prevents unexpected behaviour due to unclear input.

    Returns:
        True if the user wants to play again.
        False if the user wants to quit.
    """
    while True:
        # Ask a yes/no question and normalise the input to lower-case.
        answer = input("Do you want to play again? (y/n): ").strip().lower()

        # Accept common yes variations.
        if answer in ("y", "yes"):
            return True

        # Accept common no variations.
        if answer in ("n", "no"):
            return False

        # If the input is neither yes nor no, show a helpful message.
        print("Please type 'y' for yes or 'n' for no.")


def main():
    """
    Main entry point for the whole program.

    This function controls the overall loop:
    - It plays a single game.
    - Then asks if the user wants to play again.
    - If not, it exits gracefully.

    Using a main() function follows good practice in Python and
    makes the code more structured and testable.
    """
    while True:
        # Play one complete game of Tic Tac Toe.
        play_single_game()

        # Ask if another game should be started.
        if not ask_play_again():
            print("Thanks for playing. Goodbye!")
            break  # Exit the while loop and end the program.


# This condition ensures that main() is only executed
# when this file is run directly (not when it is imported as a module).
if __name__ == "__main__":
    main()
