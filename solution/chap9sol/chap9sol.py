##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 9장 프로젝트 기반 학숩 II - 카드게임 블랙잭
##### 작성자: 도경구 (확인 2020/12/26)

#### 9.2 카드게임 API 라이브러리 모듈

import random

### 카드 1벌 만들어 무작위로 섞기
### 실습 9.1 - fresh_deck 함수 만들기 (p.424-425)

# code : 9-1.py
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for s in suits:
        for r in ranks:
            card = (s, r)
            deck.append(card)
    random.shuffle(deck)
    return deck

deck = fresh_deck()
# # Test code
# print(deck)

### 카드 덱에서 카드 한 장 뽑아주기
# code : 9-2.py
def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return deck[0], deck[1:]

# # Test code
# card, deck = hit(deck)
# print(card)

### 실습 9.2 - count_score 함수 만들기 (p.426-427)

# code : 9-3.py
def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        rank = card[1]
        if rank == 'A':
            score += 11
            number_of_ace += 1
        elif rank in {'J','Q','K'}:
            score += 10
        else:
            score += rank
    while score > 21 and number_of_ace > 0:
        score -= 10
        number_of_ace -= 1
    return score

### 카드 프린트해서 보여주기
# code : 9-4.py
def show_cards(cards, message):
    print(message)
    for card in cards:
        print(' ',card[0],card[1])

### 카드를 더 받을지 물어보기
# code : 9-5.py
def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'


#### 9.3 프로그래밍 프로젝트 1단계 : 블랙잭

### 실습 9.3 - 카드게임 블랙잭 구현 (p.430-436)
# blackjack 폴더 참조


#### 9.5 프로그래밍 프로젝트 2단계 : 블랙잭 (기능 확장)

### 실습 9.4 - 파일에서 게임 기록 정보 읽기 함수 (p.445-446)

# code : 9-6.py
def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

### 실습 9.5 - 파일에 게임 기록 정보 쓰기 함수 (p.447)

# code : 9-7.py
def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + '\n'              
        file.write(line)
    file.close()

### 실습 9.6 - 로그인 함수 (p.448-449) 

# code : 9-8.py
def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members.keys():
        if trypasswd == members[username][0]:
            tries = members[username][1]
            wins = members[username][2]
            print("You played", tries, "games and won", wins, "of them")
            wpercent = 100*wins/tries if tries > 0 else 0 
            print("Your all-time winning percentage is", \
                  "{0:.1f}".format(wpercent), "%")
            chips = members[username][3]
            if chips >= 0:
                print("You have", chips, "chips.")
            else:
                print("You owe", -chips, "chips.")
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd,0,0,0)
        return username, 0, 0, 0, members
        
### 실습 9.7 - Top 5 보여주기 함수 (p.450-452) 

# code : 9-10.py
def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(), \
                            key=lambda x: x[1][3], \
                            reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    rank = 1
    for member in sorted_members[:5]:
        chips = member[1][3]
        if chips <= 0 :
            break
        print(rank,".",member[0],":",chips)
        rank += 1

### 실습 9.8 - 블랙잭 확장 버전 완성 (p.455) 
# blackjack+ 폴더 참조


#### 연습 문제

### 9.1 - 희소 리스트 만들기 (p.456)

# code : 9-11.py
def sparse(ns):
	dic = {}
	index = 0
	for n in ns:
		if n != 0:
			dic[index] = n
		index += 1
	return dic

# # Test code
# print(sparse([]))                        # {}
# print(sparse([0,0,3,0,0,0,0,0,0,7,0,0])) # {2: 3, 9: 7}
# print(sparse([1,0,2,0,0,0,9,0,0]))       # {0: 1, 2: 2, 6: 9}

### 9.2 - 두 희소 리스트 덧셈 (p.457)

# code : 9-12.py
def sparse_add(ms,ns):
	mvalues = ms.values()
	nvalues = ns.values()
	for key in ms:
		value = ns.get(key)
		if value != None:
			ms[key] += value
			del ns[key]
	for key in ns:
		ms[key] = ns[key]
	return ms

# # test code
# print(sparse_add({},{}))                           # {}
# print(sparse_add({2: 3, 9: 7},{}))                 # {2: 3, 9: 7}
# print(sparse_add({},{0: 1, 2: 2, 6: 9}))           # {0: 1, 2: 2, 6: 9}
# print(sparse_add({2: 3, 9: 7},{0: 1, 2: 2, 6: 9})) # {2: 5, 9: 7, 0: 1, 6: 9}




