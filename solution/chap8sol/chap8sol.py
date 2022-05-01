##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 8장 프로젝트 기반 학숩 I - 퍼즐게임 스도쿠
##### 작성자: 도경구 (확인 2020/12/26)

#### 8.1 중첩 루프

### 실습 8.1 - 가로 변형 (p.372)

def digit_art_horizontal_left_down(n):
    for i in range(1,n+1):
        for j in range(i+1):
            print(j+1, end=' ')
        print()

# # Test code
# digit_art_horizontal_left_down(7)

def digit_art_horizontal_left_up(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=' ')
        print()

# # Test code
# digit_art_horizontal_left_up(7)


### 실습 8.2 - 세로 변형 (p.373)

def digit_art_vertical_right_down(n):
    for i in range(n):
        for j in range(n):
            if n - 1 - i > j:
                print(' ', end=' ')
            else:
                print(i+1, end=' ')
        print()

def digit_art_vertical_right_down(n):
    for i in range(1,n+1):
        for _ in range(n-i):
            print(' ', end=' ')
        for _ in range(i):
            print(i,end=' ') 
        print()

def digit_art_vertical_right_down(n):
    for i in range(1,n+1):
        print("  " * (n-i) + (str(i) + " ") * i)

# # Test code
# digit_art_vertical_right_down(7)


### 실습 8.3 - 세로 방향 바꾸기 (p.375)

def digit_art_vertical_alternate(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print(i+1, end=' ')
            else:
                print(n-i, end=' ')
        print()

def digit_art_vertical_alternate(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j % 2 == 1:
                print(i,end=' ') 
            else:
                print(n-i+1,end=' ') 
        print()

def digital_art_vertical_alternate(n):
    for i in range(1, n+1):
        for _ in range(n):
            print(i, end = ' ')
            i = n - i + 1
        print()
        
# # Test code
# digit_art_vertical_alternate(7)


### 실습 8.4 - 버블정렬 구현 (p.377)

# code : 8-5.py
def bubblesort(ns):
    for k in range(len(ns)-1,0,-1): # 6, 5, 4, 3, 2, 1
        for i in range(k): # 0
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
    return ns

def bubblesort(ns):
    for k in range(len(ns)):
        for i in range(len(ns)-k-1):
            if ns[i] > ns[i+1]:
                ns[i], ns[i+1] = ns[i+1], ns[i]
    return ns

# # Test code
# print(bubblesort([32,23,18,7,11,99,55])) 
# # [7, 11, 18, 23, 32, 55, 99]


### 실습 8.5 - 기수정렬 구현 (p.378-379)

# code : 8-6.py
def radixsort(ds):
    if ds != []:
        length = len(ds[0])
        for i in range(length-1,-1,-1):
            distributed = [[] for _ in range(10)]
            for d in ds:
                distributed[int(d[i])].append(d)
            ds = []
            for d in distributed:
                ds += d
        return ds
    else:
        return []

# # Test code
# print(radixsort([]))
# print(radixsort(["239"]))
# print(radixsort(["170",'045','075','090','002','024','802','066']))
# print(radixsort(["239",'234','879','878','123','358','416','317','137','225']))
# print(radixsort(["0505", "0515", "1225", "0915", "1111", "0101", "0318", "0301"]))
# print(radixsort(["01000", "00100", "00001", "10000", "00010"]))
# # []
# # ['239']
# # ['002', '024', '045', '066', '075', '090', '170', '802']
# # ['123', '137', '225', '234', '239', '317', '358', '416', '878', '879']
# # ['0101', '0301', '0318', '0505', '0515', '0915', '1111', '1225']
# # ['00001', '00010', '00100', '01000', '10000']


#### 8.2 프로그래밍 프로젝트 : 스도쿠

import random

# code : 8-7.py (p.385)
def initialize_board_4x4():
    row0 = [1,2,3,4]
    random.shuffle(row0)
    row1 = row0[2:4] + row0[0:2]
    row2 = [row0[1], row0[0], row0[3], row0[2]]
    row3 = row2[2:4] + row2[0:2]
    return [row0, row1, row2, row3]

# code : 8-8.py (p.386)
def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

### 실습#8-6 가로세로 뒤집기 (p.387-388)
# code : 8-9.py 
def transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])
    return transposed

# # Test code
# print(transpose(b1))

# code : 8-10.py (p.388)
def create_solution_board_4x4():
    board = initialize_board_4x4()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

# code : 8-12.py (p.393)
def copy_board(board):
    board_clone = []
    for row in board :
        board_clone.append(row[:])
    return board_clone

# code : 8-13.py (p.395)
def get_level():
    level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    while level not in ("1","2","3"):
        level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    if level == "1":
        return 6
    elif level == "2":
        return 8
    else:
        return 10

### 실습 8.7 - 퍼즐보드 만들기 (p.395-396)
# code : 8-14.py
def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1        
    return board

# code : 8-15.py (p.397)
def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

# code : 8-16.py (p.397)
def get_integer(message,i,j):
    digit = input(message)
    while not (digit.isdigit() and i <= int(digit) <= j):
        digit = input(message)
    return int(digit)

# code : 8-11.py (p.390)
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

# # Test code
# sudoku_mini()

### 프로젝트 옵션 #1 : 6x6  스도쿠
### 프로젝트 옵션 #2 : 9x9  스도쿠
## 4x4 스도쿠 코드와 유사하므로 해답 코드를 제공하지 않습니다.
## 4x4 스도쿠 코드는 sudoku4x4.py 참조


#### 연습 문제

### 8.1 - 구구단 출력 (p.401-403)

### 가. 가로전개 구구단

def gugudan1():
    for i in range(2,10):
        for j in range(2,6):
            print(i, 'x', j, '=', str(i*j).rjust(2), end='  ')
        print()
        for j in range(6,10):
            print(i, 'x', j, '=', str(i*j).rjust(2), end='  ')
        print()
        print()

# # Test code
# gugudan1()

### 나. 세로전개 구구단

def gugudan2():
    for j in range(2,10):
        for i in range(2,6):
            print(i, 'x', j, '=', str(i*j).rjust(2), end='  ')
        print()
    print()
    for j in range(2,10):
        for i in range(6,10):
            print(i, 'x', j, '=', str(i*j).rjust(2), end='  ')
        print()

# # Test code
# gugudan2()

### 8.2 - ASCII Sharp 아트 (p.403-405)
# 인수는 홀수만 들어온다고 가정한다.
# 즉, 짝수 인수는 고려하지 않는다. 

# code : 8-17.py
def ascii_art(n):
    for i in range(n):
        for j in range(n):
            print('#', end=' ')
        print()

# # Test code
# ascii_art(1)
# ascii_art(3)
# ascii_art(5)
# ascii_art(7)
# 
### 가. 십자가

def ascii_art_cross(n):
  for i in range(n):
    for j in range(n):
      if i == n // 2 or j == n // 2:
        print('#', end=' ')
      else:
        print(' ', end=' ')
    print()

# # Test code
# ascii_art_cross(1)
# ascii_art_cross(3)
# ascii_art_cross(5)
# ascii_art_cross(7)

### 나. 기울인 십자가

def ascii_art_X(n):
  for i in range(n):
    for j in range(n):
      if i == j or i + j == n - 1:
        print('#', end=' ')
      else:
        print(' ', end=' ')
    print()

# # Test code
# ascii_art_X(1)
# ascii_art_X(3)
# ascii_art_X(5)
# ascii_art_X(7)

### 다. 미음

def ascii_art_square(n):
  for i in range(n):
    for j in range(n):
      if i == 0 or i == n - 1 or j == 0 or j == n - 1:
        print('#', end=' ')
      else:
        print(' ', end=' ')
    print()

# # # Test code
# ascii_art_square(1)
# ascii_art_square(3)
# ascii_art_square(5)
# ascii_art_square(7)

### 라. 마름모
def ascii_art_diamond(n):
  mid = n // 2
  for i in range(n):
    for j in range(n):
      if abs(i-j) == mid or i+j == mid or i+j == n + mid - 1:
        print('#', end=' ')
      else:
        print(' ', end=' ')
    print()

# # Test code
# ascii_art_diamond(1)
# ascii_art_diamond(3)
# ascii_art_diamond(5)
# ascii_art_diamond(7)


### 8.3 - Number 아트 (p.405-407)

# code : 8-18.py 
def numbers_art(n):
  for i in range(n):
      for j in range(n):
          print(j+1, end=' ')
      print()

# # Test code
# numbers_art(5)
# numbers_art(6)
# numbers_art(7)

## 가. 내리막

def numbers_art1(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=' ')
        print()

# # Test code
# numbers_art1(5)
# numbers_art1(6)
# numbers_art1(7)

## 나. 줄타기

def numbers_art2(n):
    for i in range(n):
        for j in range(n):
            if i <= j:
                print(j+1, end=' ')
            else:
                print(end='  ')
        print()

# # Test code
# numbers_art2(5)
# numbers_art2(6)
# numbers_art2(7)

## 다. 오끄럼

def numbers_art3(n):
    for i in range(n):
        for j in range(i+1):
            print(n-i+j, end=' ')
        print()

# # Test code
# numbers_art3(5)
# numbers_art3(6)
# numbers_art3(7)

## 라. 오르막

def numbers_art4(n):
    for i in range(n):
        for j in range(n):
            if i < n - j - 1:
                print(end='  ')
            else:
                print(j+1,end=' ')
        print()

# # Test code
# numbers_art4(5)
# numbers_art4(6)
# numbers_art4(7)


### 8.4 - 오른 뿔 그리기 (p.407-408)

def hornright(n):
    for i in range(1,n+1):
        k = i % 10
        for j in range(1,i+1):
            print(k,end=' ')
        print()
    for i in range(n-1,0,-1):
        k = i % 10
        for j in range(1,i+1):
            print(k,end=' ')
        print()

# # Test code
# hornright(-3)
# hornright(0)
# hornright(1)
# hornright(2)
# hornright(6)
# hornright(12)

### 8.5 - 로또 6/45 (p.408-409)

def lotto645():
    import random
    numbers = []
    for _ in range(6):
        number = random.randrange(1,46)
        while number in numbers:
            number = random.randrange(1,46)
        numbers.append(number)
    numbers.sort()
    for number in numbers:
        if number < 10:
            print("0"+str(number), end=" ")
        else:
            print(number, end=" ")
    print()

# for _ in range(5):
#     lotto645()


### 8.6 - 중첩 리스트에서 원소 개수 세기 (p.409-411)

# code : 8-19.py
def count_deep(xss):
    counter = 0
    for xs in xss:
        if isinstance(xs,list):
            counter += count_deep(xs)
        else:
            counter += 1
    return counter

# # Test code
# print(count_deep([1,2,3])) 
# # 3
# print(count_deep([1,[],3])) 
# # 2
# print(count_deep([1,[1,2,[3,4]]])) 
# # 5
# print(count_deep([[[[[[[[1,2,3]]]]]]]])) 
# # 3
# print(count_deep([])) 
# # 0
# print(count_deep([[[[3]],[4]],5,6,[7]])) 
# # 5
# print(count_deep([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]])) 
# # 14

# code : 8-20.py
def count_the(x,xss):
    counter = 0
    for xs in xss:
        if isinstance(xs,list):
            counter += count_the(x,xs)
        elif x == xs:
            counter += 1
    return counter

# # Test code
# print(count_the(1,[])) 
# # 0
# print(count_the(7,[1,7,7])) 
# # 2
# print(count_the(7,[1,[7],7])) 
# # 2
# print(count_the(7,[7,[2,7,[4,7]]])) 
# # 3
# print(count_the(7,[[[[[[[],[[7,2,7]],7]]]]]])) 
# # 3
# print(count_the(7,[[[[7]],[7]],5,7,[3]])) 
# # 3
# print(count_the(5,[1,[5,2],[[3],[5,4]],[[[5,5,5,5]]],6,[5,[[5],[[9]]]]])) 
# # 8

### 8.7 - 중첩 리스트 납작하게 만들기 (p.411)

# code : 8-21.py
def flatten(xss):
    flat = []
    for x in xss:
        if isinstance(x,list):
            flat += flatten(x)
        else:
            flat.append(x)
    return flat

# # Test code
# print(flatten([])) 
# # []
# print(flatten([1,2,3])) 
# # [1, 2, 3]
# print(flatten([1,[],3])) 
# # [1, 3]
# print(flatten([1,[1,2,[3,4]]])) 
# # [1, 1, 2, 3, 4]
# print(flatten([[[[[[[[1,2,3]]]]]]]])) 
# # [1, 2, 3]
# print(flatten([[[[3]],[4]],5,6,[7]])) 
# # [3, 4, 5, 6, 7]
# print(flatten([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]])) 
# # [1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9]

### 8.8 - 개수만큼 폭발 (p.412)

# code : 8-22.py
def blast(ns):
    bs = []
    for n in ns:
        ns = []
        for _ in range(n):
            ns.append(n)
        bs += ns
    return bs

# # Test code
# print(blast([]))
# # []
# print(blast([1,2,4]))
# # [1, 2, 2, 4, 4, 4, 4]
# print(blast([3,5]))
# # [3, 3, 3, 5, 5, 5, 5, 5]
# print(blast([2,-3,3]))
# # [2, 2, 3, 3, 3]

### 8.9 - 짝 찾기 (p.412-413)

# code : 8-23.py
def find_all_pairs(ns,n):
    pairs = []
    for i in range(len(ns)):
        for j in range(i+1,len(ns)):
            if ns[i] + ns[j] == n:
                pairs.append((i,j))
    return pairs

# # Test code
# print(find_all_pairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],10))
# # [(0, 1), (0, 5), (3, 4), (4, 8)]
# print(find_all_pairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],5))
# # [(0, 7), (3, 6), (3, 9), (6, 8), (8, 9)]
# print(find_all_pairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],7))
# # [(0, 3), (0, 8), (1, 7), (2, 6), (2, 9), (5, 7)]


### 8.10 4-Queen 만족 여부 확인 함수 (p.413-415)

board1 = [[0, 1, 0, 0], 
          [0, 0, 0, 1],
          [1, 0, 0, 0],
          [0, 0, 1, 0]]

board2 = [[0, 0, 1, 0], 
          [1, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 1, 0, 0]]

board3 = [[1, 0, 0, 0], 
          [0, 0, 1, 0],
          [0, 0, 0, 1],
          [0, 1, 0, 0]]

board4 = [[0, 0, 1, 0], 
          [1, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1]]

# code : 8-24.py
def transpose(mat):
    no_of_columns = len(mat[0])
    transposed = []  
    for _ in range(no_of_columns):
        transposed.append([])
    for row in mat:
        i = 0
        for entry in row:
            transposed[i].append(entry)
            i += 1
    return transposed

# code : 8-25.py
def appears_once(ns): # 1 appears only once
    count = 0
    for n in ns:
        if n == 1:
            count += 1
    return count == 1

# code : 8-26.py
def appears_more_than_once(ns): # 1 appears more than once
    count = 0
    for n in ns:
        if n == 1:
            count += 1
    return count > 1

def right_diagonals(size):
    diagonals = {}
    for k in range(2 * size - 1):
        diagonals[k] = []
    for i in range(size):
        for j in range(size):
            diagonals[i+j].append((i,j))
    return diagonals

def left_diagonals(size):
    diagonals = {}
    for k in range(2 * size - 1):
        diagonals[k] = []
    for i in range(size):
        for j in range(size):
            diagonals[i-j+3].append((i,j))
    return diagonals

def check_diagonals(diagonals,board):
    for diagonal in diagonals.values():
        ns = []
        for (i,j) in diagonal:
            ns.append(board[i][j])
        if appears_more_than_once(ns):
            return False
    return True

def check_4queen(board):
    for row in board: # check rows
        if not appears_once(row):
            return False
    for row in transpose(board): # check columns
        if not appears_once(row):
            return False
    size = len(board)
    return check_diagonals(right_diagonals(size),board) and \
           check_diagonals(left_diagonals(size),board)

# # Test code
# print(check_4queen(board1)) # True
# print(check_4queen(board2)) # True
# print(check_4queen(board3)) # False
# print(check_4queen(board4)) # False


