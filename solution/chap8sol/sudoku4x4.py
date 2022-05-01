import random

def initialize_board_4x4():
    row0 = [1, 2, 3, 4]
    random.shuffle(row0)
    row1 = [row0[2], row0[3], row0[0], row0[1]]
    row2 = [row0[1], row0[0], row0[3], row0[2]]
    row3 = [row0[3], row0[2], row0[1], row0[0]]
    board = [row0, row1, row2, row3]
    return board

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board):
    size = len(board)
    transposed = []
    for _ in range(size):
        transposed.append([])
    for row in board:
        for j in range(size):
            transposed[j].append(row[j])
    return transposed

def create_solution_board_4x4():
    board = initialize_board_4x4()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board :
        board_clone.append(row[:])
    return board_clone

def get_level():
    print("Enter Your Level.")
    level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    while level not in ("1","2","3"):
        level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    if level == "1":
        return 6
    elif level == "2":
        return 8
    else:
        return 10

def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

def get_integer(message,i,j):
    digit = input(message)
    while not (digit.isdigit() and i <= int(digit) <= j):
        digit = input(message)
    return int(digit)

def sudoku_mini():
    solution_board = create_solution_board_4x4()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    while no_of_holes > 0:
        i = get_integer("Row#(1,2,3,4): ",1,4) - 1
        j = get_integer("Column#(1,2,3,4): ",1,4) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = get_integer("Number(1,2,3,4): ",1,4)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n,": Wrong number! Try again.")
    print("Well done! Come again.")

sudoku_mini()












