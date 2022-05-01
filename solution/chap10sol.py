##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 10장 예외 처리
##### 작성자: 도경구 (확인 2020/12/27) (수정 2021/06/02)

### 실습 10.1 - 예외 발생시켜 보기 (p.463)
# 개별 확인

### 실습 10.2 - 실수 입력 확인 (p.471)

def input_float():
    while True:
        try:
            x = float(input("Enter a number: "))
        except ValueError:
            print("Not a number.")
        else:
            return x
        finally:
            print(":‑)")

# # Test code
# print(input_float())

### 실습 10.3 - 조합 계산 서비스 구현 (p.474-476)

def comb_pascal(n, r):
    vector = [1 for _ in range(r+1)]
    for _ in range(1, n - r + 1):
        for j in range(1, r + 1):
            vector[j] = vector[j-1] + vector[j]
    return vector[r]

# print("This program computes combination of two natural numbers, n and r.")
# print("Press Control-C to quit.")
# while True:
#     try:
#         n = int(input("Enter n: "))
#         r = int(input("Enter r: "))
#         assert n >= 0 and r >=0 and n >= r
#     except ValueError:
#         print("Not a number.")
#     except AssertionError:
#         print(n, "C", r, " is not defined.",sep='')
#     except KeyboardInterrupt:
#         print("Bye!")
#         break
#     else:
#         print(n, "C", r, " = ", comb_pascal(n,r), sep='')


### 실습 10.4 - 실수 입력 확인 (범위 제한) (p.477-478)

class OutOfBoundOne(Exception): pass

def input_float():
    while True:
        try:
            x = float(input("Enter a number between -1.0 and 1.0: "))
            if not (-0.1 <= x <= 1.0):
                raise OutOfBoundOne
        except ValueError:
            print("Not a number.")
        except OutOfBoundOne:
            print("Out of bound.")
        else:
            return x
        finally:
            print(":‑)")

# # Test code
# print(input_float())


#### 연습 문제

### 10.1 - 퍼즐게임 미니 스도쿠 예외 처리 추가 (p.478)


### 10.2 - 카드게임 블랙잭 예외 처리 추가 (p.478)


