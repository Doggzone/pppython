##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 4장 재귀와 반복 : 자연수 계산
##### 작성자: 도경구 (확인 2020/12/08)

#### 4.1 자연수 수열의 합 

### 실습 4.1 - 구간 수열의 합 (p.166-167)

# code : 4-10.py
def sumrange(m,n):
    if m <= n:
        return m + sumrange(m+1, n)
    else:
        return 0

# code : 4-11.py
def sumrange(m,n):
    def loop(m,sum):
        if m <= n:
            return loop(m+1,sum+m)
        else:
            return sum
    return loop(m,0)

# code : 4-12.py
def sumrange(m,n):
    sum = 0
    while m <= n:
        sum = sum + m
        m = m + 1
    return sum

# # Test code
# print(sumrange(3,2))   # 0
# print(sumrange(3,3))   # 3
# print(sumrange(3,4))   # 7
# print(sumrange(3,6))   # 18
# print(sumrange(1,10))  # 55
# print(sumrange(-5,10)) # 40
# print(sumrange(-5,-2)) # -14

#### 4.3 최대공약수

### 실습 4.2 - 최대공약수 함수 완성 (p.181)

# code : 4-21.py
def gcd(m,n):
    while n != 0:
        m, n = n, m % n
    return m

# # Test code
# print(gcd(48,18))   # 6
# print(gcd(18,48))   # 6
# print(gcd(192,72))  # 24
# print(gcd(18,57))   # 3
# print(gcd(0,11))    # 11
# print(gcd(0,0))     # 0

### 실습 4.3 - 나눠풀기 알고리즘 꼬리재귀 버전 (183-184)

# code : 4-24.py
def gcd(m,n):
    def loop(m,n,k):
        if not (m == 0 or n == 0):
            if m % 2 == 0 and n % 2 == 0:
                return loop(m//2,n//2,2*k)
            elif m % 2 == 0 and n % 2 == 1:
                return loop(m//2,n,k)
            elif m % 2 == 1 and n % 2 == 0:
                return loop(m,n//2,k)
            elif m <= n:
                return loop(m,(n-m)//2,k)
            else:
                return loop(n,(m-n)//2,k)
        else:
            if m == 0:
                return n*k
            else: # n == 0
                return m*k
    return loop(m,n,1)

# # Test code
# print(gcd(48,18))   # 6
# print(gcd(18,48))   # 6
# print(gcd(192,72))  # 24
# print(gcd(18,57))   # 3
# print(gcd(0,11))    # 11
# print(gcd(0,0))     # 0

### 실습 4.4 - 나눠풀기 알고리즘 while 루프 버전 (p.184-185)

# code : 4-25.py
def gcd(m,n):
    k = 1
    while not (m == 0 or n == 0):
        if m % 2 == 0 and n % 2 == 0:
            m, n, k = m // 2, n // 2, 2 * k
        elif m % 2 == 0 and n % 2 == 1:
            m = m // 2
        elif m % 2 == 1 and n % 2 == 0:
            n = n // 2
        elif m <= n:
            n = (n - m) // 2
        else:
            m, n = n, (m - n) // 2
    if m == 0:
        return n*k
    else: # n == 0
        return m*k

# # Test code
# print(gcd(48,18))   # 6
# print(gcd(18,48))   # 6
# print(gcd(192,72))  # 24
# print(gcd(18,57))   # 3
# print(gcd(0,11))    # 11
# print(gcd(0,0))     # 0

#### 4.4 곱셈

### 실습 4.5 - 덧셈/뺄셈 알고리즘 : 꼬리재귀 함수 버전 (p.186-187)

# code : 4-27.py
def mult(m,n):
    def loop(n,ans):
        if n > 0:
            return loop(n-1,m+ans)
        else:
            return ans
    return loop(n,0)

# # Test code
# print(mult(3,6)) # 18
# print(mult(0,6)) # 0
# print(mult(3,0)) # 0
# print(mult(0,0)) # 0

### 실습 4.6 - 덧셈/뺄셈 알고리즘 : while 루프 버전 (p.187-188)

# code : 4-28.py
def mult(m,n):
    ans = 0
    while n > 0:
        n, ans = n - 1, m + ans
    return ans

# # Test code
# print(mult(3,6)) # 18
# print(mult(0,6)) # 0
# print(mult(3,0)) # 0
# print(mult(0,0)) # 0

### 실습 4.7 - 덧셈/뺄셈/절반 알고리즘 : 재귀 함수 버전  (p.188-189)

# code : 4-29.py
def fastmult(m,n):
    if n > 0:
        if n % 2 == 0:
            return fastmult(m+m,n//2)
        else:
            return m + fastmult(m,n-1)
    else:
        return 0

# # Test code
# print(fastmult(3,6)) # 18
# print(fastmult(0,6)) # 0
# print(fastmult(3,0)) # 0
# print(fastmult(0,0)) # 0

### 실습 4.8 - 덧셈/뺄셈/절반 알고리즘 : 꼬리재귀 함수 버전 (p.189-190)

# code : 4-30.py
def fastmult(m,n):
    def loop(m,n,ans):
        if n > 0:
            if n % 2 == 0:
                return loop(m+m,n//2,ans)
            else:
                return loop(m,n-1,m+ans)
        else:
            return ans
    return loop(m,n,0)

# # Test code
# print(fastmult(3,6)) # 18
# print(fastmult(0,6)) # 0
# print(fastmult(3,0)) # 0
# print(fastmult(0,0)) # 0

### 실습 4.9 - 덧셈/뺄셈/반나누기 알고리즘 : while 루프 버전 (p.190-191) 

# code : 4-31.py
def fastmult(m,n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            m, n = m + m, n // 2
        else:
            n, ans = n - 1, m + ans
    return ans

# # Test code
# print(fastmult(3,6)) # 18
# print(fastmult(0,6)) # 0
# print(fastmult(3,0)) # 0
# print(fastmult(0,0)) # 0


### 실습 4.10 - 러시아 농부 알고리즘 : 재귀 함수 버전 (p.192)

# code : 4-32.py
def russian_mult(m,n):
    def loop(m,n):
        if n > 1:
            if n % 2 == 1:
                return m + loop(m+m,n//2)
            else:
                return loop(m+m,n//2)
        else: # n == 0
            return m
    if n > 0:
        return loop(m,n)
    else:
        return 0

# # Test code
# print(russian_mult(57,86)) # 4902
# print(russian_mult(57,0))  # 0
# print(russian_mult(0,86))  # 0
# print(russian_mult(0,0))   # 0

### 실습 4.11 - 러시아 농부 알고리즘 : 꼬리재귀 함수 버전 (p.193)

# code : 4-33.py
def russian_mult(m,n):
    def loop(m,n,a):
        if n > 1:
            if n % 2 == 1:
                return loop(m+m,n//2,a+m)
            else:
                return loop(m+m,n//2,a)
        else: # n == 0
            return a+m
    if n > 0:
        return loop(m,n,0)
    else:
        return 0

# # Test code
# print(russian_mult(57,86)) # 4902
# print(russian_mult(57,0))  # 0
# print(russian_mult(0,86))  # 0
# print(russian_mult(0,0))   # 0

### 실습 4.12 - 러시아 농부 알고리즘 : while 루프 버전 (p.194)

# code : 4-34.py
def russian_mult(m,n):
    if n > 0:
        a = 0
        while n > 1:
            if n % 2 == 1:
                a = a + m
            m = m + m
            n = n // 2
        return a+m
    else:
        return 0

# # Test code
# print(russian_mult(57,86)) # 4902
# print(russian_mult(57,0))  # 0
# print(russian_mult(0,86))  # 0
# print(russian_mult(0,0))   # 0


#### 연습 문제

### 4.1 - 카운트다운 타이머 (p.195)

from time import sleep

def countdown2(n) :
    if n > 0 :
        if n < 10 and n % 2 == 0:
            print("발사임박!")
        else:
            print(n)
        sleep(1)
        countdown2(n-1)
    else :
        print("발사!")

def countdown2(n):
    while n > 0 :
        if n < 10 and n % 2 == 0:
            print("발사임박!")
        else:
            print(n)
        sleep(1)
        n = n - 1
    print("발사!")

# # Test code
# countdown2(15)


### 4.2 - 팩토리얼 (p.197)

# code : 4-37.py
def fac(n):
    if n > 0:
        return fac(n-1) * n
    else:
        return 1

# code : 4-38.py
def fac(n):
    def loop(n,p):
        if n > 0:
            return loop(n-1,p*n)
        else:
            return p
    return loop(n,1)

# code : 4-39.py
def fac(n):
    ans = 1
    while n > 0:
        n, ans = n - 1, ans * n
    return ans

def fac(n):
    ans = 1
    while n > 0:
        ans = ans * n
        n = n - 1
    return ans

# # Test code
# print(fac(0))  # 1
# print(fac(1))  # 1
# print(fac(5))  # 120
# print(fac(9))  # 362880
# print(fac(15)) # 1307674368000
# print(fac(30)) # 265252859812191058636308480000000


### 4.3 - 삼각수 (p.198)

# code : 4-40.py
def trinum(n):
    if n >= 1:
        return n + trinum(n-1)
    else:
        return 0

def trinum(n):
    def loop(n,r):
        if n >= 1:
            return loop(n-1,n+r)
        else:
            return r
    return loop(n,0)

def trinum(n):
    r = 0
    while n >= 1:
        r += n
        n -= 1
    return r

# # Test code
# print(trinum(1))  # 1
# print(trinum(3))  # 6
# print(trinum(6))  # 21
# print(trinum(11)) # 66
# print(trinum(0))  # 0
# print(trinum(-3)) # 0

### 4.4 - 덧셈만 가지고 제곱 계산하기 (p.199)

# code : 4-41.py
def square(n):
    def loop(n):
        if n > 0:
            return n + n - 1 + loop(n-1)
        else:
            return 0
    return loop(abs(n))

def square(n):
    def loop(n,sum):
        if n > 0:
            return loop(n-1,sum+n+n-1)
        else:
            return sum
    return loop(abs(n),0)

def square(n):
    n = abs(n)
    sum = 0
    while n > 0:
        sum = sum + n + n - 1
        n = n - 1
    return sum

# # Test code
# print(square(0))  # 0
# print(square(1))  # 1
# print(square(-2)) # 4
# print(square(3))  # 9
# print(square(-4)) # 16
# print(square(5))  # 25

### 4.5 - 순열 (p.200-201)

# 음수는 고려하지 않는다.
# 그리고  n < k 인 경우에는 0을 내주도록 한다.

# code : 4-42.py
def permutation(n,k):
    if k > 0:
        return n * permutation(n-1,k-1)
    else:
        return 1

def permutation(n,k):
    def loop(n,k,p):
        if k > 0:
            return loop(n-1,k-1,p*n)
        else:
            return p
    return loop(n,k,1)

def permutation(n,k):
    p = 1
    while k > 0:
        p *= n
        n -= 1
        k -= 1
    return p

# # Test code
# print(permutation(1,1)) # 1
# print(permutation(2,1)) # 2
# print(permutation(2,2)) # 2
# print(permutation(3,1)) # 3
# print(permutation(3,2)) # 6
# print(permutation(3,3)) # 6
# print(permutation(4,1)) # 4
# print(permutation(4,2)) # 12
# print(permutation(4,3)) # 24
# print(permutation(4,4)) # 24
# print(permutation(4,5)) # 0


### 4.6 - 급수 계산 (p.201)

# code : 4-43.py
def sum_of_num_over_next(n):
    if n > 0:
        return n / (n + 1) + sum_of_num_over_next(n-1)
    else:
        return 0

def sum_of_num_over_next(n):
    def loop(n,sum):
        if n > 0:
            return loop(n-1,n/(n+1)+sum)
        else:
            return sum
    return loop(n,0)

def sum_of_num_over_next(n):
    sum = 0
    while n > 0:
        sum += n / (n + 1)
        n -= 1
    return sum

# # Test code
# print(sum_of_num_over_next(0))   # 0
# print(sum_of_num_over_next(1))   # 0.5
# print(sum_of_num_over_next(3))   # 1.9166666666666665
# print(sum_of_num_over_next(5))   # 3.5500000000000003
# print(sum_of_num_over_next(10))  # 7.980122655122655
# print(sum_of_num_over_next(100)) # 95.80272149226131
# 약간의 오차는 문제삼지 않습니다.

### 4.7 - 정수 범위의 합 (p.201-202)

# code : 4-44.py
def add_range(start,stop,step):
    if start < stop:
        return start + add_range(start+step,stop,step)
    else:
        return 0

def add_range(start,stop,step):
    def loop(start,sum):
        if start < stop:
            return loop(start+step,sum+start)
        else:
            return sum
    return loop(start,0)
    
def add_range(start,stop,step):
    sum = 0
    while start < stop:
        start, sum = start + step, sum + start
    return sum

# # Test code
# print(add_range(1,10,1)) # 45
# print(add_range(1,10,2)) # 25
# print(add_range(1,10,3)) # 12
# print(add_range(-5,6,2)) # 0


### 4.8 - 오늘부터 n일 뒤는 몇 년 몇 월 며칠? (p.202-204)

# code : 4-46.py
def isleapyear(year):
    # assume year >= 0
    return year % 400 == 0 or \
           year % 4 == 0 and year % 100 != 0

# code : 4-47.py
def next_month(year, month):
    # assume year >= 0 and 1 <= month <= 12
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return (year, month)

# code : 4-48.py
def days_in_month(year, month):
    # assume year >= 0 and 1 <= month <= 12
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isleapyear(year):
            return 29
        else:
            return 28

# code : 4-45.py
def date_after_n_days(year, month, day, n):
    # assume that is_valid_date(year, month, day) is True
    days_left = days_in_month(year,month) - day
    if days_left < n:
        n -= days_left
        (year, month) = next_month(year, month)
        days_this_month = days_in_month(year, month)
        while days_this_month < n:
            n -= days_this_month
            (year, month) = next_month(year, month)
            days_this_month = days_in_month(year,month)
        return (year, month, n)
    else:
        return (year, month, day + n)

# # Test code   
# print(date_after_n_days(2019,4,20,2))    # (2019, 4, 22)
# print(date_after_n_days(2019,4,20,7))    # (2019, 4, 27)
# print(date_after_n_days(2019,4,20,10))   # (2019, 4, 30)
# print(date_after_n_days(2019,4,20,11))   # (2019, 5, 1)
# print(date_after_n_days(2019,4,20,50))   # (2019, 6, 9)
# print(date_after_n_days(2019,4,20,100))  # (2019, 7, 29)
# print(date_after_n_days(2019,4,20,200))  # (2019, 11, 6)
# print(date_after_n_days(2019,4,20,300))  # (2020, 2, 14)
# print(date_after_n_days(2019,4,20,1000)) # (2022, 1, 14)


### 4.9 - 자연수 수열의 합 : 나눠풀기 알고리즘 (p.204-206) 

# code : 4-49.py
# recursion
def sigma2(n):
    # assert n > 0
    if n > 1:
        if n % 2 == 0:
            n = n // 2
            return 2 * sigma2(n) + n * n
        else:
            return n + sigma2(n-1)
    else:
        return 1

# tail recursion
def sigma2(n):
    def loop(n, m, acc):
        if n > 1:
            if n % 2 == 0:
                n //= 2
                return loop(n, m*2, acc+n*n*m)
            else:
                return loop(n-1, m, acc+n*m)
        else:
            return m + acc
    return loop(n,1,0)

# while loop
def sigma2(n):
    m = 1
    acc = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
            acc += n * n * m
            m *= 2
        else:
            acc += n * m
            n -= 1
    return m + acc

# # Test code
print(sigma2(13))       # 91
print(sigma2(12))       # 78
print(sigma2(11))       # 66
print(sigma2(10))       # 55
print(sigma2(9))        # 45
print(sigma2(8))        # 36
print(sigma2(7))        # 28
print(sigma2(6))        # 21
print(sigma2(5))        # 15
print(sigma2(4))        # 10
print(sigma2(3))        # 6
print(sigma2(2))        # 3
print(sigma2(1))        # 1
print(sigma2(47733))    # 1139243511
print(sigma2(37387282)) # 698904446367403




