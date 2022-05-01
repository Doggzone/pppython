def copy_board(board):
    board_clone = []
    for row in board:
        board_clone.append(row[:])
    return board_clone