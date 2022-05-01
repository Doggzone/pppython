##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 5장 재귀와 반복 : 정렬
##### 작성자: 도경구 (확인 2020/12/25)

#### 5.1 시퀀스

### 실습 5.1 - for 루프 작성 연습 (p.222-224)

# code : 5-2.py
from time import sleep
def countdown(n):
	for i in range(n,0,-1):
		print(i)
		sleep(1)
	print("Launch!")

# # Test code
# countdown(10)

# code : 5-4.py
def sigma(n):
    sum = 0
    for i in range(n,0,-1):
    	sum = sum + i
    return sum

# # Test code
# print(sigma(10))

# code : 5-6.py
def sumrange(m,n):
    sum = 0
    for i in range(m,n+1):
    	sum = sum + i
    return sum

# # Test code
# print(sumrange(3,2))   # 0
# print(sumrange(3,3))   # 3
# print(sumrange(3,4))   # 7
# print(sumrange(3,6))   # 18
# print(sumrange(1,10))  # 55
# print(sumrange(-5,10)) # 40
# print(sumrange(-5,-2)) # -14

# code : 5-8.py
def fac(n):
    ans = 1
    for k in range(n,1,-1):
        ans = k * ans
    return ans

# # Test code
# print(fac(1)) # 1
# print(fac(5)) # 120

# code : 5-10.py
def power(b,n):
    prod = 1
    for i in range(n,0,-1):
    	prod = prod * i
    return prod

# # Test code
# print(power(2,5)) # 120

#### 5.2 리스트 정렬

### 실습 5.2 - insert : 재귀 함수 버전 (p.233)

# code : 5-17.py
def insert(x,ss):
    if ss != []:
        if x <= ss[0]:
            return [x] + ss
        else:
            return [ss[0]] + insert(x,ss[1:])
    else:
        return [x]

# # Test code
# print(insert(1,[2,4,5,7,8])) # [1, 2, 4, 5, 7, 8]
# print(insert(6,[2,4,5,7,8])) # [2, 4, 5, 6, 7, 8]
# print(insert(9,[2,4,5,7,8])) # [2, 4, 5, 7, 8, 9]
# print(insert(9,[])) # [9]

### 실습 5.3 - insert : 꼬리재귀 함수 버전 (p.234-235)

# code : 5-18.py
def insert(x,ss): 
    def loop(ss,left):
        if ss != []:
            if x <= ss[0]:
                left.append(x)
                return left+ss
            else:
                left.append(ss[0])
                return loop(ss[1:],left)
        else:
            left.append(x)
            return left
    return loop(ss,[])

# # Test code
# print(insert(1,[2,4,5,7,8])) # [1, 2, 4, 5, 7, 8]
# print(insert(6,[2,4,5,7,8])) # [2, 4, 5, 6, 7, 8]
# print(insert(9,[2,4,5,7,8])) # [2, 4, 5, 7, 8, 9]
# print(insert(9,[])) # [9]

### 실습 5.4 - insert : while 루프 버전  (p.235-236)

# code : 5-19.py
def insert(x,ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            left.append(x)
            return left+ss 
        else:
            left.append(ss[0])
            ss = ss[1:]
    left.append(x)
    return left

# # Test code
# print(insert(1,[2,4,5,7,8])) # [1, 2, 4, 5, 7, 8]
# print(insert(6,[2,4,5,7,8])) # [2, 4, 5, 6, 7, 8]
# print(insert(9,[2,4,5,7,8])) # [2, 4, 5, 7, 8, 9]
# print(insert(9,[])) # [9]

### 실습 5.5 - insertion_sort : 꼬리재귀 함수 버전  (p.236-237)

# code : 5-21.py
def insertion_sort(xs):
    def loop(xs,ss):
        if xs != []:
            return loop(xs[1:],insert(xs[0],ss))
        else:
            return ss
    return loop(xs,[])

# # Test code
# print(insertion_sort([3,5,4,2])) # [2, 3, 4, 5]

### 실습 5.6 - insertion_sort : while 루프 버전 (p.237)

# code : 5-22.py
def insertion_sort(xs) :
    ss = []
    while xs != []:
        xs, ss = xs[1:], insert(xs[0],ss)
    return ss

# # Test code
# print(insertion_sort[3,5,4,2])) # [2, 3, 4, 5]

### 실습 5.7 - insertion_sort : for 루프 버전 (p.238)

# code : 5-23.py
def insertion_sort(xs):
    ss = []
    for x in xs:
        ss = insert(x,ss)
    return ss

# # Test code
# print(insertion_sort([3,5,4,2])) # [2, 3, 4, 5]

### 실습 5.8 - merge : 꼬리재귀 함수 버전 (p.242)

# code : 5-26.py
def merge(left,right):
    def loop(left,right,ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                return loop(left[1:],right,ss)
            else:
                ss.append(right[0])
                return loop(left,right[1:],ss)
        else:
            return ss + left + right
    return loop(left,right,[])

# # Test code
# print(merge([18,23,32],[7,11,55,99])) # [7, 11, 18, 23, 32, 55, 99]

### 실습 5.9 - merge : while 루프 버전 (p.242-243)

# code : 5-27.py
def merge(left,right):
    ss = []
    while not (left == [] or right == []):
        if left[0] <= right[0]:
            ss.append(left[0])
            left = left[1:]
        else:
            ss.append(right[0])
            right = right[1:]
    return ss + left + right

# # Test code
# print(merge([18,23,32],[7,11,55,99])) # [7, 11, 18, 23, 32, 55, 99]

### 실습 5.10 - partition : 꼬리재귀 함수 버전 (p.247)

# code : 5-30.py
def partition(pivot,xs):
    def loop(xs,ls,rs):
        if xs != []:
            if xs[0] <= pivot:
                ls.append(xs[0])
            else:
                rs.append(xs[0])
            return loop(xs[1:],ls,rs)
        else:
            return ls, rs
    return loop(xs,[],[]) 

### 실습 5.11 - partition : while 루프 버전 (p.248)

# code : 5-31.py
def partition(pivot,xs):
    ls, rs = [], []
    while xs != []:
        if xs[0] <= pivot:
            ls.append(xs[0])
        else:
            rs.append(xs[0])
        xs = xs[1:]
    return ls, rs

### 실습 5.12 - partition : for 루프 버전 (p.248)

# code : 5-32.py
def partition(pivot,xs):
    ls, rs = [], []
    for x in xs:
        if x <= pivot:
            ls.append(x)
        else:
            rs.append(x)
    return ls, rs

# print(partition(5,[7,2,1,9,4]))
# print(partition(3,[5]))


#### 연습문제

### 5.1 - 팰린드롬 검사 함수 (p.249)

# code : 5-33.py
# def ispalindrome(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     else:
#         return ispalindrome(s[1:-1])

# code : 5-34.py
def ispalindrome(s):
    return len(s) <= 1 or s[0] == s[-1] and ispalindrome(s[1:-1])

# # Test code
# print(ispalindrome("")) # True
# print(ispalindrome("a")) # True
# print(ispalindrome("aa")) # True
# print(ispalindrome("aba")) # True
# print(ispalindrome("abba")) # True
# print(ispalindrome("aaba")) # False
# print(ispalindrome("abcba")) # True
# print(ispalindrome("여보 안경 안 보여")) # False
# print(ispalindrome("여보안경안보여")) # True

### 5.2 - 삼각수 (for 루프 버전) (p.250)

def trinum(n):
    r = 0
    for i in range(n,0,-1):
        r = r + i
    return r

# # Test code
# print(trinum(1))  # 1
# print(trinum(3))  # 6
# print(trinum(6))  # 21
# print(trinum(11)) # 66
# print(trinum(0))  # 0
# print(trinum(-3)) # 0

### 5.3 - 덧셈만 가지고 제곱 계산하기 (for 루프 버전) (p.250)

def square(n):
    n = abs(n)
    sum = 0
    for k in range(1,n+1):
        sum = sum + k + k - 1
    return sum

# # Test code
# print(square(0))  # 0
# print(square(1))  # 1
# print(square(-2)) # 4
# print(square(3))  # 9
# print(square(-4)) # 16
# print(square(5))  # 25

### 5.4 - 순열 (for 루프 버전) (p.250)

def permutation(n,k):
    p = 1
    for i in range(n,n-k,-1): # range(n-k+1,n+1)
        p *= i
    return p

# # Test code
# print(permutation(1,1)) # => 1
# print(permutation(2,1)) # => 2
# print(permutation(2,2)) # => 2
# print(permutation(3,1)) # => 3
# print(permutation(3,2)) # => 6
# print(permutation(3,3)) # => 6
# print(permutation(4,1)) # => 4
# print(permutation(4,2)) # => 12
# print(permutation(4,3)) # => 24
# print(permutation(4,4)) # => 24

### 5.5 - 급수 계산 (for 루프 버전) (p.250)

def sum_of_num_over_next(n):
    sum = 0
    for i in range(1,n+1):
        sum += i / (i + 1)
    return sum

# # Test code
# print(sum_of_num_over_next(0))   # 0
# print(sum_of_num_over_next(1))   # 0.5
# print(sum_of_num_over_next(3))   # 1.9166666666666665
# print(sum_of_num_over_next(5))   # 3.5500000000000003
# print(sum_of_num_over_next(10))  # 7.980122655122655
# print(sum_of_num_over_next(100)) # 95.80272149226131
# 실수 계산 오차로 결과가 약간 다를 수 있습니다.

### 5.6 - 윤년 출력 프로시저 (p.251)

# code : 5-35.py
def is_leap_year(year):
    return year % 400 == 0 or \
           year % 4 == 0 and year % 100 != 0

def print_leap_year(yearfrom, yearto):
    print("Leap years between", yearfrom, "and", yearto, ":")
    for y in range(yearfrom, yearto+1):
        if is_leap_year(y):
            print(y)

# # Test code
# print_leap_year(1990,2004) # 1992 1996 2000 2004를 한 줄에 하나씩 프린트
# print_leap_year(2005,2014) # 2008 2012를 한 줄에 하나씩 프린트
# print_leap_year(2094,2106) # 2096 2104를 한 줄에 하나씩 프린트

### 5.7 - ISBN-10 코드 검증 (p.252)

def isbn10(s):
    total = 0
    for i in range(1,10):
        total = total + int(s[i-1]) * i
    last = total % 11
    if last == 10:
        return s[9] == "X"
    else:
        return s[9] == str(last)

# # Test code
# print(isbn10("123456789X")) # True
# print(isbn10("1234567890")) # False
# print(isbn10("1413304540")) # True
# print(isbn10("141330454X")) # False


### 5.8 - 문자열 빈칸 채우기 (p.253)

# code : 5-36.py
def fillwith_(sentence):
    new_sentence = ''
    for char in sentence:
        if char == ' ':
            new_sentence = new_sentence + '_'
        else:
            new_sentence = new_sentence + char
    return new_sentence

# # Test code
# print(fillwith_('따스한 봄 나들이 갑시다.')) 
# # '따스한_봄_나들이_갑시다.'
# print(fillwith_('아름다운 가을 단풍 구경하러 산으로 갑시다.'))
# # '아름다운_가을_단풍_구경하러_산으로_갑시다.'
# print(fillwith_("나는 프로그래밍을 공부할 수 있어 너무 행복합니다."))
# # '나는_프로그래밍을_공부할_수_있어_너무_행복합니다.'

### 5.9 - 모음 일련번호 매기기 (p.253-254)

# code : 5-37.py
def vowel_numbering(word):
    number = 1
    newword = ''
    for c in word:
        if c in ['a','e','i','o','u','A','E','I','O','U']:
            newword = newword + str(number) 
            number = number + 1
        else:
            newword = newword + c
    return newword

# # Test code
# print(vowel_numbering('Massachussettes')) # 'M1ss2ch3ss4tt5s'


### 5.10 - 재귀 함수를 꼬리재귀, while 루프, for 루프 함수로 변환하기 (p.254-255)

# code : 5-38.py
def updown(ns):
    if ns != []:
        if ns[0] % 2 == 0:
            return [ns[0]//2] + updown(ns[1:])
        else:
            return [ns[0]*2] + updown(ns[1:])
    else:
        return []

# 꼬리재귀 버전 1
def updown(ns):
    def loop(ns,ss):
        if ns != []:
            if ns[0] % 2 == 0:
                return loop(ns[1:],ss+[ns[0]//2])
            else:
                return loop(ns[1:],ss+[ns[0]*2])
        else:
            return ss
    return loop(ns,[])

# 꼬리재귀 버전 2
def updown(ns):
    def loop(ns,ss):
        if ns != []:
            if ns[0] % 2 == 0:
                ss.append(ns[0]//2)
                return loop(ns[1:],ss)
            else:
                ss.append(ns[0]*2)
                return loop(ns[1:],ss)
        else:
            return ss
    return loop(ns,[])

# while 루프 버전
def updown(ns):
    ss = []
    while ns != []:
        if ns[0] % 2 == 0:
            ss.append(ns[0]//2)
        else:
            ss.append(ns[0]*2)
        ns = ns[1:]
    return ss

# for 루프 버전
def updown(ns):
    ss = []
    for n in ns:
        if n % 2 == 0:
            ss.append(n//2)
        else:
            ss.append(n*2)
    return ss

# # Test code
# print(updown([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
# #            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
# print(updown([14, 69,   87, 13, 0, 16,  83, 19, 45, 88]))
# #            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]


### 5.11 - 부분 리스트 (p.255-258)

### (가) drop_before 함수

# code : 5-40.py
def drop_before(s,index):
    while s != [] and index > 0:
        s = s[1:]
        index -= 1
    return s

# # Test code
# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]")
# print("drop_before(s,0) =", drop_before(s,0)) # [1, 2, 3, 4, 5]
# print("drop_before(s,1) =", drop_before(s,1)) # [2, 3, 4, 5]
# print("drop_before(s,2) =", drop_before(s,2)) # [3, 4, 5]
# print("drop_before(s,3) =", drop_before(s,3)) # [4, 5]
# print("drop_before(s,4) =", drop_before(s,4)) # [5]
# print("drop_before(s,5) =", drop_before(s,5)) # []
# print("drop_before(s,6) =", drop_before(s,6)) # []
# print("drop_before(s,-3) =", drop_before(s,-3)) # [1, 2, 3, 4, 5]
# print("drop_before([],4) =", drop_before([],4)) # []

### (나) take_before 함수

# code : 5-41.py
# 재귀 버전
def take_before(s,index):
    if s != [] and index > 0:
        return [s[0]] + take_before(s[1:],index-1)
    else:
        return []

# 꼬리재귀 버전
def take_before(s,index):
    def loop(s,index,ss):
        if s != [] and index > 0:
            ss.append(s[0])
            return loop(s[1:],index-1,ss)
        else:
            return ss
    return loop(s,index,[])

# while 루프 버전
def take_before(s,index):
    ss = []
    while s != [] and index > 0:
        ss.append(s[0])
        s = s[1:]
        index -= 1
    return ss

# # Test code
# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]")
# print("take_before(s,0) =", take_before(s,0)) # []
# print("take_before(s,1) =", take_before(s,1)) # [1]
# print("take_before(s,2) =", take_before(s,2)) # [1, 2]
# print("take_before(s,3) =", take_before(s,3)) # [1, 2, 3]
# print("take_before(s,4) =", take_before(s,4)) # [1, 2, 3, 4]
# print("take_before(s,5) =", take_before(s,5)) # [1, 2, 3, 4, 5]
# print("take_before(s,6) =", take_before(s,6)) # [1, 2, 3, 4, 5]
# print("take_before([],4) =", take_before([],4)) # []
# print("take_before(s,-3) =", take_before(s,-3)) # []

### (다) sublist 함수

# code : 5-42.py
def sublist(s,low,high):
    if low < 0: low = 0
    if high < 0: high = 0
    if low <= high:
        return take_before(drop_before(s,low),high-low)
    else:
        return []

# # Test code
# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]") # 
# print("sublist(s,0,0) => [] ?", sublist(s,0,0)) # []
# print("sublist(s,0,1) => [1] ?", sublist(s,0,1)) # [1]
# print("sublist(s,0,2) => [1, 2] ?", sublist(s,0,2)) # [1, 2]
# print("sublist(s,0,3) => [1, 2, 3] ?", sublist(s,0,3)) # [1, 2, 3]
# print("sublist(s,0,4) => [1, 2, 3, 4] ?", sublist(s,0,4)) # [1, 2, 3, 4]
# print("sublist(s,0,5) => [1, 2, 3, 4, 5] ?", sublist(s,0,5)) # [1, 2, 3, 4, 5]
# print("sublist(s,0,6) => [1, 2, 3, 4, 5] ?", sublist(s,0,6)) # [1, 2, 3, 4, 5]
# print("sublist(s,1,1) => [] ?", sublist(s,1,1)) # []
# print("sublist(s,1,2) => [2] ?", sublist(s,1,2)) # [2]
# print("sublist(s,1,3) => [2, 3] ?", sublist(s,1,3)) # [2, 3]
# print("sublist(s,1,4) => [2, 3, 4] ?", sublist(s,1,4)) # [2, 3, 4]
# print("sublist(s,1,5) => [2, 3, 4, 5] ?", sublist(s,1,5)) # [2, 3, 4, 5]
# print("sublist(s,1,6) => [2, 3, 4, 5] ?", sublist(s,1,6)) # [2, 3, 4, 5]
# print("sublist(s,2,2) => [] ?", sublist(s,2,2)) # []
# print("sublist(s,2,3) => [3] ?", sublist(s,2,3)) # [3]
# print("sublist(s,2,4) => [3, 4] ?", sublist(s,2,4)) # [3, 4]
# print("sublist(s,2,5) => [3, 4, 5] ?", sublist(s,2,5)) # [3, 4, 5]
# print("sublist(s,2,6) => [3, 4, 5] ?", sublist(s,2,6)) # [3, 4, 5]
# print("sublist(s,3,3) => [] ?", sublist(s,3,3)) # []
# print("sublist(s,3,4) => [4] ?", sublist(s,3,4)) # [4]
# print("sublist(s,3,5) => [4, 5] ?", sublist(s,3,5)) # [4, 5]
# print("sublist(s,3,6) => [4, 5] ?", sublist(s,3,6)) # [4, 5]
# print("sublist(s,5,2) => [] ?", sublist(s,5,2)) # []
# print("sublist(s,-3,-2) => [] ?", sublist(s,-3,-2)) # []


### 5.12 - 이웃과 차이 줄이기 (p.259-260)

# code : 5-43.py
def reduce_diff(ns):
    if len(ns) > 1:
        if ns[0] < ns[1]:
            return [ns[0]+1] + reduce_diff(ns[1:])
        elif ns[0] > ns[1]:
            return [ns[0]-1] + reduce_diff(ns[1:])
        else:
            return [ns[0]] + reduce_diff(ns[1:])
    else:
        return ns

# # Test code
# print(reduce_diff([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#                 # [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(reduce_diff([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#                 # [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(reduce_diff([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(reduce_diff([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(reduce_diff([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# (1) 꼬리재귀 함수 버전
def reduce_diff(ns):
    def loop(ns,rs):
        if len(ns) > 1:
            if ns[0] < ns[1]:
                rs.append(ns[0]+1)
            elif ns[0] > ns[1]:
                rs.append(ns[0]-1)
            else:
                rs.append(ns[0])
            return loop(ns[1:],rs)
        else:
            rs.append(ns[0])
            return rs
    return loop(ns,[])

# # Test code
# print(reduce_diff([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#                 # [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(reduce_diff([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#                 # [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(reduce_diff([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(reduce_diff([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(reduce_diff([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# (2) while 루프 함수 버전
def reduce_diff(ns):
    rs = []
    while len(ns) > 1:
        if ns[0] < ns[1]:
            rs.append(ns[0]+1)
        elif ns[0] > ns[1]:
            rs.append(ns[0]-1)
        else:
            rs.append(ns[0])
        ns = ns[1:]
    rs.append(ns[0])
    return rs

# # Test code
# print(reduce_diff([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#                 # [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(reduce_diff([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#                 # [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(reduce_diff([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(reduce_diff([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(reduce_diff([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# (3) for 루프 함수 버전
def reduce_diff(ns):
    current = ns[0]
    pairs = []
    for n in ns[1:]:
        pairs.append((current,n))
        current = n
    rs = []
    for (n0, n1) in pairs:
        if n0 < n1:
            rs.append(n0+1)
        elif n0 > n1:
            rs.append(n0-1)
        else:
            rs.append(n0)
    rs.append(ns[-1])
    return rs

# # Test code
# print(reduce_diff([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#                 # [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(reduce_diff([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#                 # [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(reduce_diff([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(reduce_diff([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(reduce_diff([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#                 # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

### 5.13 - 동일화 (p.260-261)

# code : 5-44.py
# # 리스트의 원소가 모두 같은지 확인
def allequal(ns):
    if len(ns) > 1:
        first = ns[0]
        for n in ns[1:]:
            if first != n:
                return False
        return True
    else:
        return True

def equalizer(ns):
    count = 0
    if len(ns) > 1:
        while not allequal(ns):
            ns = reduce_diff(ns)
            count += 1
    return count

# # Test code
# print(equalizer([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))          # 9
# print(equalizer([8, 2, 5, 7, 1, 1, 6, 7, 4, 8]))          # 12
# print(equalizer([8, 4, 5, 6, 9, 8, 6, 2, 0, 6]))          # 14   
# print(equalizer([4, 0, 1, 0, 3, 4, 3, 3, 7, 9]))          # 13
# print(equalizer([1, 6, 5, 6, 8, 5, 3, 3, 3, 8]))          # 13
# print(equalizer([]))                                      # 0
# print(equalizer([5]))                                     # 0
# print(equalizer([4, 4, 4]))                               # 0
# print(equalizer([4, 3]))                                  # 1
# print(equalizer([4, 5]))                                  # 1
# print(equalizer([4, 5, 4]))                               # 2
# print(equalizer([14, 69, 87, 13, 0, 16, 83, 19, 45, 88])) # 92


### 5.14 - 부분 문자열 (p.261-263)
### 가. substrings_of_length 함수

# code : 5-45.py
def substrings_of_length(k,s):
	if k == 0:
		return ['']
	elif 0 < k <= len(s):
		subs = []
		for i in range(len(s)-k+1):
			subs.append(s[i:i+k])
		return subs
	else:
		return None

# # Test code
# print(substrings_of_length(0,"ERICA")) # ['']
# print(substrings_of_length(1,"ERICA")) # ['E', 'R', 'I', 'C', 'A']
# print(substrings_of_length(2,"ERICA")) # ['ER', 'RI', 'IC', 'CA']
# print(substrings_of_length(3,"ERICA")) # ['ERI', 'RIC', 'ICA']
# print(substrings_of_length(4,"ERICA")) # ['ERIC', 'RICA']
# print(substrings_of_length(5,"ERICA")) # ['ERICA']
# print(substrings_of_length(6,"ERICA")) # None

### 나. substrings 함수

# code : 5-46.py
def substrings(s):
	subs = ['']
	for k in range(1,len(s)+1):
		subs += substrings_of_length(k,s)
	return subs

# # Test code
# print(substrings("ERICA"))
# # ['', 'E', 'R', 'I', 'C', 'A', 'ER', 'RI', 'IC', 'CA', 'ERI', 'RIC', 'ICA', 'ERIC', 'RICA', 'ERICA']
# print(substrings(""))
# # ['']


### 5.15 -- 진수 변환 (p.263-266)
### 가. 2진수를 10진수로 바꾸기

# code : 5-47.py
def bin2dec(bin):
    length = len(bin)
    dec = 0
    for i in range(length):
        if bin[i] == '1':
            dec += 2**(length-i-1)
    return dec

# # Test code
# print(bin2dec('0'))      # 0
# print(bin2dec('1'))      # 1
# print(bin2dec('110'))    # 6
# print(bin2dec('10011'))  # 19
# print(bin2dec('101010')) # 42

### 나. 10진수를 2진수로 바꾸기

# code : 5-48.py
def dec2bin(dec):
    bin = ''
    while not (dec == 0 or dec == 1):
        r = dec % 2
        bin = str(r) + bin
        dec = dec // 2
    bin = str(dec) + bin
    return bin

# # Test code
# print(dec2bin(0))  # '0'
# print(dec2bin(1))  # '1'
# print(dec2bin(6))  # '110'
# print(dec2bin(19)) # '10011'
# print(dec2bin(42)) # '101010'

### 5.16 - 이진수 덧셈 (p.267-268)
### 자리수는 같다고 가정
### 숫자열은 '0' 또는 '1'로만 구성된다.

# code : 5-49.py
def add_binary(n1,n2):
    over = 0
    answer = ''
    for d in range(-1,-len(n1)-1,-1):
        total = int(n1[d]) + int(n2[d]) + over
        if total == 1:
            over = 0
            answer = '1' + answer
        elif total == 2:
            over = 1
            answer = '0' + answer
        elif total == 3:
            over = 1
            answer = '1' + answer
        else: # total = 0
            over = 0
            answer = '0' + answer
    if over == 1:
        answer = '1' + answer
    return answer

# # Test code
# print(add_binary('',''))                 # ''
# print(add_binary('0','0'))               # '0'
# print(add_binary('1','0'))               # '1'
# print(add_binary('0','1'))               # '1'
# print(add_binary('1','1'))               # '10'
# print(add_binary('10','11'))             # '101'
# print(add_binary('11','11'))             # '110'
# print(add_binary('1011','1101'))         # '11000'
# print(add_binary('1111','1111'))         # '11110'
# print(add_binary('11011001','00011011')) # '11110100'





