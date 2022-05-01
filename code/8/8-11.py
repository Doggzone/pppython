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