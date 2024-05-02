BOARD_SIZE = 3


def new_board():
    """
    >>> new_board()
    [[None, None, None], [None, None, None], [None, None, None]]
    """
    return [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def render_board(board):
    """
    >>> board = new_board()
    >>> board[0][0] = "X"
    >>> board[1][2] = "O"
    >>> board[2][1] = "X"
    >>> render_board(board)
        0 1 2
       -------
    0 | X     |
    1 |     O |
    2 |   X   |
       -------
    """
    print("    0 1 2")
    print("   -------")
    for row in range(BOARD_SIZE):
        print(f"{row} | ", end="")
        for col in range(BOARD_SIZE):
            print(board[row][col] or " ", end=" ")
        print("|")
    print("   -------")


def get_move(board):
    while True:
        try:
            row, col = map(
                int, input("Enter row and column (0~2), separated by a space: ").split()
            )
            if row < 0 or row > BOARD_SIZE - 1 or col < 0 or col > BOARD_SIZE - 1:
                print("Invalid input, please try again.")
                continue
            if board[row][col] is not None:
                print("This cell is already taken, please try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input, please try again.")
