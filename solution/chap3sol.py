##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 3장 제어 구조
##### 작성자: 도경구 (확인 2020/12/08)

#### 3.1 논리식

### 실습 3.1 - 짝수 확인 함수 (p.100)

# code : 3-1.py
def even(n):
    return n % 2 == 0

# print(even(13)) # False
# print(even(26)) # True

#### 3.2 선택문

### 실습 3.2 - 흐름도 그리기 (p.106)

# 스스로

### 실습 3.3 - 즁첩 선택문의 실행 경로 따져보기 (p.108)

# 스스로

### 실습 3.4 - 둘 중 작은 수 찾기 함수 (p.108-109)

# code : 3-7.py
def smaller(x,y):
    if x < y:
        return x
    else:
        return y

# # Test code
# print(smaller(3,5)) # returns 3
# print(smaller(5,3)) # returns 3
# print(smaller(3,3)) # returns 3

### 실습 3.5 - 셋 중 가장 작은 수 찾기 함수 (p.109)

# code : 3-8.py
def smallest(x,y,z):
    if x < y:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z

# # Test code
# print(smallest(3,5,9)) # returns 3
# print(smallest(5,3,9)) # returns 3
# print(smallest(5,9,3)) # returns 3
# print(smallest(3,9,5)) # returns 3
# print(smallest(9,3,5)) # returns 3
# print(smallest(9,5,3)) # returns 3
# print(smallest(3,3,5)) # returns 3
# print(smallest(5,3,3)) # returns 3
# print(smallest(3,5,3)) # returns 3
# print(smallest(3,3,3)) # returns 3

### 실습 3.6 - 셋 중 가장 작은 수 찾기 함수 (smaller 활용) (p.110)

# code : 3-9.py
def smallest(x,y,z):
    return smaller(smaller(x,y),z)

# # Test code
# print(smallest(3,5,9)) # returns 3
# print(smallest(5,3,9)) # returns 3
# print(smallest(5,9,3)) # returns 3
# print(smallest(3,9,5)) # returns 3
# print(smallest(9,3,5)) # returns 3
# print(smallest(9,5,3)) # returns 3
# print(smallest(3,3,5)) # returns 3
# print(smallest(5,3,3)) # returns 3
# print(smallest(3,5,3)) # returns 3
# print(smallest(3,3,3)) # returns 3

#### 3.3 반복문

### 실습 3.7 - 수강과목 평균 점수 계산 서비스 (p.115-117)

# # code : 3-13.py
# print("Score Average Calculator")
# number = int(input("How many classes? "))
# total = 0
# count = 0
# while count < number:
#     score = int(input("Enter your score: "))
#     total += score # total = total + score
#     count += 1 # count = count + 1
# print("Your average score =", end=' ')
# if count > 0:
#     print(round(total/number, 1))
# else:
#     print("0.0")


### 실습 3.8 - 수강과목 평균 점수 계산 서비스 (입력 확인) (p.122)

# print("Score Average Calculator")
# number = input("How many classes? ")
# while not number.isdigit():
#     number = input("Enter positive number only: ")
# number = int(number)
# total = 0
# count = 0
# while count < number:
#     score = input("Enter your score: ")
#     while not (score.isdigit() and 0 <= int(score) <= 100):
#         score = input("Your score must be between 0 and 100: ")
#     total += int(score)
#     count += 1
# print("Your average score =", end=' ')
# if count > 0:
#     print(round(total/count, 1))
# else:
#     print("0.0")

#### 3.4 문자열 해부

### 실습 3.9 - 정수 문자열 확인 함수 (음수 포함) (p.127-128)

# code : 3-15.py
def isinteger(s):
    return s.isdigit() or \
           s != '' and s[0] == '-' and s[1:].isdigit()

# # Test code
# print(isinteger("55"))    # True
# print(isinteger("5o5"))   # False
# print(isinteger("-55"))   # True
# print(isinteger("--55"))  # False
# print(isinteger("---55")) # False
# print(isinteger("5-5"))   # False
# print(isinteger("55-"))   # False
# print(isinteger("+55"))   # False
# print(isinteger("five"))  # False
# print(isinteger("-"))     # False
# print(isinteger(""))      # False


### 실습 3.10 - 실수 문자열 확인 함수 (음수 포함) (p.128-129)

# code : 3-16.py
def isfloat(s):
    (num, dot, fraction) = s.partition('.')
    return dot == '' and fraction == '' and isinteger(num) or \
           dot == '.' and \
           ((num == '' or num == '-') and fraction.isdigit() or \
            fraction == '' and isinteger(num) or \
            isinteger(num) and fraction.isdigit())

# # Test code
# print(isfloat(".112"))   # True
# print(isfloat("-.112"))  # True
# print(isfloat("3.14"))   # True
# print(isfloat("-3.14"))  # True
# print(isfloat("5."))     # True
# print(isfloat("5.0"))    # True
# print(isfloat("-777.0")) # True
# print(isfloat("-777."))  # True
# print(isfloat("."))      # False
# print(isfloat(".."))     # False



##### 연습 문제

### 3.1 - 윤년 확인 함수 (p.130-131)

# code : 3.17.py
def isleapyear(year):
	if year >= 0:
		return year % 400 == 0 or \
		       year % 4 == 0 and year % 100 != 0
	else:
		return None

# # Test code
# for y in range(5):
#     print(y, isleapyear(y))
# # True False False False True
# for y in range(2010,2017):
#     print(y, isleapyear(y))
# # False False True False False False True
# for y in range(1900, 2600, 100):
#     print(y, isleapyear(y))
# # False True False False False True False
# print(-2000, isleapyear(-2000))
# # None

### 3.2 - 유효 날짜 검증 함수 (p.131-132)

# code : 3.18.py
def is_valid_date(year,month,day):
    return year >= 0 and 1 <= month <= 12 and \
           ((month == 1 or month == 3 or month == 5 or month == 7 or
             month == 8 or month == 10 or month == 12) and 
            1 <= day <= 31 or 
            (month == 4 or month == 6 or month == 9 or month == 11) and 
            1 <= day <= 30 or 
            isleapyear(year) and 1 <= day <= 29 or 
            1 <= day <= 28) 

# # Test code
# print(is_valid_date(2020,11,31)) # False
# print(is_valid_date(2020,2,29))  # True


### 3.3 - 주민등록번호 검증 함수 (p.132-133)

def front_ok(s):
    year = int(s[:2])
    month = int(s[2:4])
    day = int(s[4:6])
    century = s[-1]
    if century == 1 or century == 2 or century == 5 or century == 6:
        year = year + 1900
    elif century == 3 or century == 4 or century == 7 or century == 8:
        year = year + 2000
    elif century == 9 or century == 0: 
        year = year + 1800
    return is_valid_date(year,month,day)

def back_ok(s):
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    e = int(s[4])
    f = int(s[5])
    g = int(s[7])
    h = int(s[8])
    i = int(s[9])
    j = int(s[10])
    k = int(s[11])
    l = int(s[12])
    m = 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11)
    if m == 11 or m == 10:
        m = m - 10
    return m == int(s[13])

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front+back[0]) and mid == "-" and back_ok(s)

# Test your RRN number
print(isRRN("000101-0000000")) # True
print(isRRN("991231-9999991")) # True

### 3.4 - 셋 중 가운데 수 찾기 함수 (p.133-134)

def median(x,y,z):
    one = smallest(x,y,z)
    if one == x:
        return smaller(y,z)
    elif one == y:
        return smaller(x,z)
    else:
        return smaller(x,y)

# # Test code
# print(median(1,3,5)) # 3
# print(median(3,5,1)) # 3
# print(median(3,3,3)) # 3
# print(median(3,5,3)) # 3
# print(median(3,5,5)) # 5 

### 3.5 - 셋 중 가장 작은 홀수 찾기 함수 (p.134-135)

def even(x):
    return x % 2 == 0

def smaller_odd(x,y):
    if even(x) and even(y):
        return None
    elif even(x):
        return y
    elif even(y):
        return x
    else:
        if x <= y:
            return x
        else:
            return y
        
def smallest_odd(x,y,z):
    smaller = smaller_odd(x,y)
    if smaller == None:
        if even(z):
            return None
        else:
            return z
    else:
        return smaller_odd(smaller,z)

# # Test code
# print(smallest_odd(3,2,2))  # 3 
# print(smallest_odd(3,5,7))  # 3 
# print(smallest_odd(3,5,1))  # 1 
# print(smallest_odd(8,3,4))  # 3
# print(smallest_odd(8,3,5))  # 3
# print(smallest_odd(8,5,3))  # 3
# print(smallest_oddd(2,8,3)) # 3
# print(smallest_odd(2,8,4))  # None    

### 3.6 - 이차방정식 근 구하는 함수 (p.135-136)

import math
def quadratic_equation_positive(a,b,c):
    if a != 0:
        delta = b**2 - 4 * a * c
        if delta > 0:
            root = math.sqrt(delta)
            return (-b + root) / 2 * a, (-b - root) / 2 * a
        else:
            return None
    else:
        return None

# print(quadratic_equation_positive(1,-1,-2)) # (2.0, -1.0)
# print(quadratic_equation_positive(3,3,3)) # None
# print(quadratic_equation_positive(0,3,4)) # None

### 3.7 - 수강과목 점수 평균 구하기 프로시저 (과락 제외 버전) (p.136-137)

# print("Score Average Calculator")
# number = input("How many classes? ")
# while not (number.isdigit() and int(number) > 0):
#     number = input("Enter a positive number: ")
# print("The number of classes =", number)
# total = 0
# passed = 0
# failed = 0
# while passed + failed < int(number):
#     score = input("Enter your score: ")
#     while not (score.isdigit() and 0 <= int(score) <= 100):
#         score = input("Enter your score between 0 and 100: ")
#     print("Your score =", score)
#     if int(score) < 60:
#         failed = failed + 1
#     else:
#         total = total + int(score)
#         passed = passed + 1
# if passed > 0:
#     print("Your average score =", round(total/passed,1))
# else:
#     print("Your average score = 0.0")
# print("Failed =", failed)

### 3.8 - 24시간 시계 형식 확인 (p.137-138)

# code : 3-23.py
def validclock24(time):
    (hour, colon, minute) = time.partition(":")
    return len(hour) == 2 and len(minute) == 2 and \
           colon == ":" and \
           0 <= int(hour) <= 23 and 0 <= int(minute) <= 59 or \
           int(hour) == 24 and int(minute) == 0

# # Test code
# print(validclock24("00:00"))  # True
# print(validclock24("00:30"))  # True
# print(validclock24("09:58"))  # True
# print(validclock24("12:15"))  # True
# print(validclock24("23:59"))  # True
# print(validclock24("24:00"))  # True
# print(validclock24("7:07"))   # False
# print(validclock24("07:121")) # False
# print(validclock24("13:4"))   # False
# print(validclock24("00:60"))  # False
# print(validclock24("24:01"))  # False
# print(validclock24("25:10"))  # False

### 3.9 - 12시간 시계 형식 확인 (p.138-139)

# code : 3-24.py
def validclock12(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]
    return (len(hour) == 1 and 1 <= int(hour) <= 9 or \
            len(hour) == 2 and 10 <= int(hour) <= 12) and \
           colon == ":" and \
           len(minute) == 2 and 0 <= int(minute) <= 59 and \
           (am_or_pm == "am" or am_or_pm == "pm")

# # Test code
# print(validclock12("1:30am"))  # True
# print(validclock12("9:12pm"))  # True
# print(validclock12("3:05am"))  # True
# print(validclock12("10:14pm")) # True
# print(validclock12("11:59pm")) # True
# print(validclock12("12:00am")) # True
# print(validclock12("12:00pm")) # True
# print(validclock12("0:15am"))  # False
# print(validclock12("09:18pm")) # False
# print(validclock12("3:5am"))   # False
# print(validclock12("00:00pm")) # False
# print(validclock12("5:60am"))  # False

### 3.10 - 24시간 시계를 12시간 시계로 변환 (p.140)

# code : 3-25.py
def clock24to12(time):
    (hour, colon, minute) = time.partition(":")
    if int(hour) == 0 or int(hour) == 24:
        return "12" + colon + minute + "am"
    elif int(hour) < 12:
        return hour + colon + minute + "am"
    elif int(hour) == 12:
        return hour + colon + minute + "pm"
    else: # int(hour) > 12
        return str(int(hour)-12) + colon + minute + "pm"

# # Test code
# print(clock24to12("00:00")) # "12:00am"
# print(clock24to12("00:05")) # "12:05am"
# print(clock24to12("09:58")) # "9:58am"
# print(clock24to12("11:43")) # "11:43am"
# print(clock24to12("12:08")) # "12:08pm"
# print(clock24to12("15:50")) # "3:50pm"
# print(clock24to12("20:20")) # "8:20pm"
# print(clock24to12("24:00")) # "12:00am"

### 3.11 - 12시간 시계를 24시간 시계로 변환 (p.140-141)

# code : 3-26.py
def clock12to24(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]
    if am_or_pm == "am" and hour == "12":
        hour = "00"
    elif am_or_pm == "pm" and hour == "12":
        hour = "12"
    elif am_or_pm == "pm":
        hour = str(int(hour)+12)
    if len(hour) < 2:
        hour = "0" + hour
    return hour + colon + minute

# # Test code
# print(clock12to24("12:00am")) # "00:00"
# print(clock12to24("12:05am")) # "00:05"
# print(clock12to24("1:30am"))  # "01:30"
# print(clock12to24("3:05am"))  # "03:05"
# print(clock12to24("12:00pm")) # "12:00"
# print(clock12to24("12:08pm")) # "12:08"
# print(clock12to24("3:50pm"))  # "15:50"
# print(clock12to24("9:12pm"))  # "21:12"
# print(clock12to24("11:59pm")) # "23:59"

### 3.12 - 종료 시간 계산하기 (p.142)

# code : 3-27.py
def minutes_after(time, minuteplus):
    (hour,":",minute) = time.partition(":")
    hourplus = minuteplus // 60
    minuteplus = minuteplus % 60
    hour = int(hour) + hourplus
    minute = int(minute) + minuteplus
    if minute > 59:
        hour += 1
        minute -= 60
    return str(hour) + ":" + str(minute)

# # Test code
# print(minutes_after("3:34",100))   # "5:14"
# print(minutes_after("11:45",20))   # "12:5"
# print(minutes_after("9:59",1))     # "10:0"
# print(minutes_after("123:10",200)) # "126:30"

### 3.13 - 소요 시간 계산하기 (p.142-143)

# code : 3-28.py
def time_passed(fromTime, toTime):
    (hour1,":",minute1) = fromTime.partition(":")
    (hour2,":",minute2) = toTime.partition(":")
    hour = int(hour2) - int(hour1)
    if minute1 > minute2:
        hour -= 1
        minute = int(minute2) + 60 - int(minute1)
    else:
        minute = int(minute2) - int(minute1)
    return str(hour) + ":" + str(minute)
    
# # Test code
# print(time_passed("03:12","03:25")) # "0:13"
# print(time_passed("11:45","13:15")) # "1:30"
# print(time_passed("06:15","07:45")) # "1:30"
# print(time_passed("03:34","05:00")) # "1:26"

### 3.14 - 시간 더하기 (p.143-144)

# code : 3-29.py
def addtime(time1,time2):
    (hour1,":",time1) = time1.partition(":")
    (minute1,":",second1) = time1.partition(":")
    (hour2,":",time2) = time2.partition(":")
    (minute2,":",second2) = time2.partition(":")
    second = int(second1) + int(second2)
    minute = int(minute1) + int(minute2)
    hour = int(hour1) + int(hour2)
    if second >= 60:
        second -= 60
        second += 1
    if minute >= 60:
        minute -= 60
        hour += 1
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    if second < 10:
        second = "0" + str(second)
    else:
        second = str(second)
    return str(hour) + ":" + minute + ":" + second

# # Test code
# print(addtime("0:14:57","0:25:02")) # "0:39:59"
# print(addtime("0:14:57","0:51:01")) # "1:05:58"
# print(addtime("0:14:57","0:51:18")) # "1:06:15"
# print(addtime("9:43:57","8:51:45")) # "18:35:42"

### 3.15 - 이진수 시프트(좌우로 밀기) 연산 (p.144-145)

# code : 3-30.py
def shift(ds,move):
    if move < 0:
        if len(ds) > abs(move):
            return ds[:move]
        else:
            return "0"
    else:
        return ds + "0" * move

# # Test code
# print(shift("11011",3)) # 11011000
# print(shift("11011",2)) # 1101100
# print(shift("11011",1)) # 110110
# print(shift("11011",0)) # 11011
# print(shift("11011",-1)) # 1101
# print(shift("11011",-2)) # 110
# print(shift("11011",-3)) # 11
# print(shift("11011",-4)) # 1
# print(shift("11011",-5)) # 0
# print(shift("11011",-6)) # 0

