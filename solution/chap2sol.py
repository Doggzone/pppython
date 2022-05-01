##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 2장 변수와 함수
##### 작성자: 도경구 (확인 2020/12/05)

#### 2.1 변수

### 실습 2.1 - 키보드 입력과 반올림 (p.66)

# radius = float(input("Enter the radius: "))
# from math import pi
# area = pi * radius ** 2
# print("The area of a circle with radius", radius, "is", round(area,1))

### 실습 2.2 - 동전 합산 서비스 (p.67)

# print("Enter the number of coins you have.")
# coin500 = int(input("500 won? "))
# coin100 = int(input("100 won? "))
# coin50 = int(input("50 won? "))
# coin10 = int(input("10 won? "))
# total = coin500 * 500 + coin100 * 100 + coin50 * 50 + coin10 * 10
# print("You have", total, "won in total.")

### 실습 2.3 - 온도 변환 서비스 (p.72)

# print("Fahrenheit to Celsius conversion")
# f = int(input("Degrees in Fahrenheit? "))
# c = (f - 32) * 5 / 9
# print(round(c,1), "degrees in Celsius")


#### 2.2 함수

### 실습 2.4 - 동전 합산 함수 (p.83)

# code : 2-17.py
def coin_in_total(c500, c100, c50, c10):
    return c500 * 500 + c100 * 100 + c50 * 50 + c10 * 10

# print("Enter the number of coins you have.")
# coin500 = int(input("500 won? "))
# coin100 = int(input("100 won? "))
# coin50 = int(input("50 won? "))
# coin10 = int(input("10 won? "))
# total = coin_in_total(coin500, coin100, coin50, coin10)
# print("You have", total, "won in total.") 

### 실습 2.5 - 온도 변환 함수 (p.84)

# code : 2-18.py
def fahrenheit2celsius(f):
    return (f - 32) * 5 / 9

# # Test code
# print(fahrenheit2celsius(67)) # 19.444444444444443
# print(round(fahrenheit2celsius(67),1)) # 19.4


### 실습 2.6 - 9의 보수 계산 함수 (p.85)

# code : 2-19.py
def compliment_nine(n):
    return 10 ** len(str(n)) - 1 - n

# # Test code
# print(complement_nine(0)) # 9 
# print(complement_nine(9)) # 0 
# print(complement_nine(4)) # 5 
# print(complement_nine(18)) # 81 
# print(complement_nine(40)) # 59 
# print(complement_nine(307)) # 692 
# print(complement_nine(9142)) # 857 
# print(complement_nine(9965)) # 34 
# print(complement_nine(9999)) # 0


##### 연습 문제

### 2.1 - 온도 변환 함수 (p.87)

# code : 2-20.py
def celsius2fahrenheit(c):
    return 9 / 5 * c + 32
    
# Test code
# print(celsius2fahrenheit(19.4)) # 66.92
# print(round(celsius2fahrenheit(19.4),1)) # 66.9


### 2.2 - 대출 원리금 균등분할 상환금 계산 (p.87~89)
### 가. 함수 구현

# code : 2-21.py
def monthly_payment_plan(principal, interest, year):
    rate_monthly = interest / 100 / 12
    compound = (1 + rate_monthly) ** (year * 12)
    return int(compound * principal * rate_monthly / (compound - 1))

# # 테스트코드
# print(monthly_payment_plan(10000000, 2.8, 4)) # should print 220460

### 나. 서비스 구현

# # 대출 상환금 계산 서비스
# # 대출금 상환금액을 계산해주는 프로그램
# #
# # 입력: 원금(principal) - 백만이상 정수만 입력한다고 가정
# #      연이자율(interest rate) - 0.0 에서 9.9 사이의 실수만 입력한다고 가정
# #      상환기간(years) - 1 이상정수만 입력한다고 가정
# # 출력: 월상환금액, 상환금액의 총계
# #
# # 작성자: 도경구
# # 작성날짜: 2019년 7월 4일 (version 1.0)

# # 입력
# print("자유은행 대출 상환금 계산 서비스에 오심을 환영합니다.")
# principal = int(input("대출원금이 얼마인가요? (백만원이상) "))
# interest = float(input("연 이자율은 몇% 인가요? (0.0~9.9) "))
# year = int(input("상환기간은 몇 년인가요? "))

# # 상환금 계산
# rate_yearly = interest / 100
# rate_monthly = rate_yearly / 12
# month = year * 12
# compound = (1 + rate_monthly) ** month
# payment_monthly = int(compound * principal * rate_monthly / (compound - 1))

# # 출력
# print()
# print("대출 상환금 내역을 알려드리겠습니다.")
# print("대출원금:", principal, "원")
# print("연 이자율", interest, "%로", year, "년 동안 매월 원리금 균등 상환")
# print("매월", payment_monthly, "원씩 지불하셔야 합니다.")
# print("상환 완료시까지 총 상환금액은", payment_monthly * 12 * year, "원 입니다.")
# print()
# print("저희 자유은행은 항상 여러분과 함께 합니다.")
# print("또 들려주세요.")




