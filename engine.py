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
