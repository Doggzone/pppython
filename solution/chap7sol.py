##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 7장 표채워풀기
##### 작성자: 도경구 (확인 2020/12/26)

#### 7.2 조합

### 실습 7.1 - comb 함수의 실행 시간 측정 함수 (p.342)

# code : 7-7.py
def comb(n,r):
    if r != 0 and r != n:
        return comb(n-1,r-1) + comb(n-1,r)
    else:
        return 1

# # Test code
# print(comb(30,3))  # 4060
# print(comb(30,27)) # 4060
# print(comb(30,7))  # 2035800
# print(comb(30,23)) # 2035800
# print(comb(30,10)) # 30045015 - 좀 오래 걸림
# print(comb(30,20)) # 30045015 - 좀 오래 걸림
# print(comb(30,15)) # 155117520 - 매우 오래 걸림

def run_comb(n,r):
    from time import perf_counter
    start = perf_counter()
    answer = comb(n,r)
    finish = perf_counter()
    print("comb(", n, ",", r, ") => ", answer, sep="")
    print(round(finish-start,4), "seconds")

# # Test code
# run_comb(30,3)  # 4060 - 0.001 seconds
# run_comb(30,27) # 4060 - 0.0011 seconds
# run_comb(30,7)  # 2035800 - 0.5204 seconds
# run_comb(30,23) # 2035800 - 0.5472 seconds
# run_comb(30,10) # 30045015 - 7.8143 seconds
# run_comb(30,20) # 30045015 - 7.9519 seconds
# run_comb(30,15) # 155117520 - 41.1853 seconds

### 실습 7.2 - comb_pascal 함수의 실행 시간 측정 (p.349)

# code : 7-8.py
def comb_pascal(n, r):
    row0 = [1 for _ in range(r+1)]
    matrix = [row0] + [[1] for _ in range(n-r)]
    for i in range(1, n - r + 1):
        for j in range(1, r + 1):
            newvalue = matrix[i][j - 1] + matrix[i - 1][j]
            matrix[i].append(newvalue)
    return matrix[n - r][r]

def run_comb_pascal(n,r):
    from time import perf_counter
    start = perf_counter()
    answer = comb_pascal(n,r)
    finish = perf_counter()
    print("comb_pascal(", n, ",", r, ") => ", answer, sep="")
    print(round(finish-start,4), "seconds")

# # Test code
# run_comb_pascal(30,3)  # 4060 - 0.0 seconds
# run_comb_pascal(30,27) # 4060 - 0.0 seconds
# run_comb_pascal(30,7)  # 2035800 - 0.0001 seconds
# run_comb_pascal(30,23) # 2035800 - 0.0 seconds
# run_comb_pascal(30,10) # 30045015 - 0.0001 seconds
# run_comb_pascal(30,20) # 30045015 - 0.0001 seconds
# run_comb_pascal(30,15) # 155117520 - 0.0001 seconds


#### 7.3 1까지 줄이는 최소 스텝

### 실습 7.3 - 표채워풀기 알고리즘 구현 (p.357)

# code : 7-13.py
def minsteps(n):
    memo = [0 for _ in range(n+1)]
    for i in range(2,n+1):
        steps = memo[i-1]
        if i % 2 == 0:
            steps = min(steps, memo[i//2])
        if i % 3 == 0:
            steps = min(steps, memo[i//3])
        memo[i] = steps + 1
    return memo[n]

def run_minsteps(n):
    from time import perf_counter
    start = perf_counter()
    answer = minsteps(n)
    finish = perf_counter()
    print("minsteps(", n, ") => ", answer, sep="")
    print(round(finish-start), "seconds")

# # Test code
# print(run_minsteps(3))       # 1
# print(run_minsteps(4))       # 2
# print(run_minsteps(7))       # 3
# print(run_minsteps(10))      # 3
# print(run_minsteps(23))      # 6
# print(run_minsteps(237))     # 8
# print(run_minsteps(317))     # 10
# print(run_minsteps(514))     # 8
# print(run_minsteps(711))     # 9
# print(run_minsteps(908))     # 11
# print(run_minsteps(1000))    # 9
# print(run_minsteps(2020))    # 10
# print(run_minsteps(1111111)) # 19

#### 7.4 하노이의 탑

### 실습 7.4 - tower_of_hanoi 함수의 실행 시간 예측 (p.362)

# 28개 = 약 1분
# 29개 = 약 2분
# 30개 = 약 4분
# 31개 = 약 8분
# 32개 = 약 16분
# 33개 = 약 32분
# 34개 = 약 64분 = 1시간 4분
# 35개 = 약 128분 = 2시간 8분
# 36개 = 약 256분 = 4시간 16분
# 37개 = 약 512분 = 8시간 32분
# 38개 = 약 1024분 = 17시간 4분
# 39개 = 약 2048분 = 34시간 8분


#### 연습 문제

### 7.1 - 설탕 최적 배송 (p.363-364)

# code : 7-16.py (재귀 버전)
def minbags(n):
    if n > 1:
        if n == 2 or n == 3 or n == 5:
            return 1
        else:
            smallest = minbags(n-2)
            if n > 4:
                smallest = min(smallest, minbags(n-3))
            if n > 6:
                smallest = min(smallest, minbags(n-5))
        return 1 + smallest
    else:
        return 0

# code : 7-17.py (Test function)
def run_minbags(n):
    from time import perf_counter
    start = perf_counter()
    answer = minbags(n)
    finish = perf_counter()
    print("minbags(", n, ") => ", answer, sep="")
    print(round(finish-start,1), "seconds")

# # Test code
# for i in range(36,51):
#     run_minbags(i)

# 표채워풀기 버전
def minbags(n):
    bags = [0,0,1,1,2,1,2]
    if n > 6:
        i = 7
        while i <= n:
            smallest = min(bags[i-2], bags[i-3], bags[i-5])
            bags.append(smallest+1)
            i += 1
    return bags[n]

# # Test code
# for i in range(36,51):
#     run_minbags(i)


### 7.2 - 달나라 토끼를 위한 구매대금 지불 도우미 (p.364-366)

# 표채워풀기 버전
def change(total):
    # coin = 1, 2, 5, 7
    counts = [0] * (total + 1)
    counts[1] = 1
    for n in range(2,total+1):
        if 2 <= n < 5:
            coins = [2]
        elif 5 <= n < 7:
            coins = [2,5]
        else:
            coins = [2,5,7] 
        minimum = counts[n-1] + 1
        for coin in coins:
            minimum = min(minimum,counts[n-coin]+1)
        counts[n] = minimum
    return counts[total]

# # Test code
# print(change(1))  # 1
# print(change(2))  # 1
# print(change(3))  # 2
# print(change(4))  # 2
# print(change(5))  # 1
# print(change(6))  # 2
# print(change(7))  # 1
# print(change(8))  # 2
# print(change(9))  # 2
# print(change(10)) # 2
# print(change(11)) # 3
# print(change(12)) # 2
# print(change(13)) # 3
# print(change(14)) # 2
# print(change(15)) # 3
# print(change(16)) # 3
# print(change(17)) # 3
# print(change(18)) # 4
# print(change(19)) # 3
# print(change(20)) # 4
# print(change(21)) # 3
# print(change(22)) # 4
# print(change(23)) # 4
# print(change(24)) # 4
# print(change(25)) # 5
# print(change(26)) # 4
# print(change(27)) # 5
# print(change(28)) # 4


