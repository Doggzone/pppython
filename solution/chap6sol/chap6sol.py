##### 프로그래밍의 정석, 파이썬 - 실습 및 연습 문제 풀이
##### 6장 재귀와 반복 : 검색
##### 작성자: 도경구 (확인 2020/12/25)

#### 6.2 이분검색

### 실습 6.1 - 논리 연산자로 흐름 제어 (p.282)

# code : 6-11.py
def bin_search_OX(ss,x):
    mid = len(ss) // 2
    return ss != [] and \
           (x == ss[mid] or \
            x < ss[mid] and bin_search_OX(ss[:mid],x) or \
            bin_search_OX(ss[mid+1:],x))

# Test code
# s = [3,5,8,7,4,6,1,9,2]
# s.sort()
# print(bin_search_OX(s,5))  # True
# print(bin_search_OX(s,8))  # True
# print(bin_search_OX(s,1))  # True
# print(bin_search_OX(s,11)) # False

#### 6.5 문자열 검색

### 실습 6.2 - find_1st 함수 테스트 (p.299-300)

# code : 6-15.py
def find_1st(filename,x):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(x)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(position) + " the 1st time.\n")
    outfile.close()
    infile.close()
    print("Done")

# # Test code
# find_1st('article.txt','computer')    # at 3269 the 1st time.
# find_1st('article.txt','Whole Earth') # at 10735 the 1st time.
# find_1st('article.txt','Apple')       # at 4380 the 1st time.
# find_1st('article.txt','apple')       # not found.

### 실습 6.3 - find_2nd 함수 테스트 (p.301)

# code : 6-16.py
def find_2nd(filename,x):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(x)
    position = text.find(x,position+1)
    if position == -1:
        outfile.write(x + " is not found.\n")
    else:
        outfile.write(x + " is at " + str(position) + " the 2nd time.\n")
    outfile.close()
    infile.close()
    print("Done")

# # Test code
# find_2nd('article.txt','computer')    # at 3357 the 2nd time.
# find_2nd('article.txt','Whole Earth') # at 11280 the 2nd time.
# find_2nd('article.txt','Apple')       # at 4455 the 2nd time.
# find_2nd('article.txt','apple')       # not found.


### 실습 6.4 - 마지막 문자열 하나만 찾기 (p.301-302)

# code : 6-17.py
def find_last(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    found_most_recent = -1
    position = text.find(key)
    while position != -1 :
        found_most_recent = position
        position = text.find(key,position+1)
    if found_most_recent == -1:
        outfile.write(key + " is not found.\n")
    else:
        outfile.write(key + " is at " + str(found_most_recent) + " the last time.\n")
    outfile.close()
    infile.close()
    print("Done")

# # Test code
# find_last('article.txt','computer')    # at 10975 the last time.
# find_last('article.txt','Whole Earth') # at 11280 the last time.
# find_last('article.txt','Apple')       # at 6604 the last time.
# find_last('article.txt','apple')       # not found.

### 실습 6.5 - 모두 찾기 (p.303)

# code : 6-18.py
def find_all(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    if position == -1:
        outfile.write(key + " is not found.\n")
    while position != -1 :
        outfile.write(key + " is at " + str(position) + ".\n")
        position = text.find(key,position+1)
    outfile.close()
    infile.close()
    print("Done")

# # Test code
# find_all('article.txt','computer')
# at 3269, 3357, 3601, 3725, 6209, 10975.
# find_all('article.txt','Whole Earth')
# at 10735, 11280.
# find_all('article.txt','Apple')
# at 4380, 4455, 4742, 5586, 5765, 6346, 6379, 6445, 6604.
# find_all('article.txt','apple')
# not found

### 실습 6.6 - 모두 찾고, 찾은 개수 세기 (p.304)

# code : 6-19.py
def find_all_count(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    count = 0
    while position != -1 :
        outfile.write(key + " is at " + str(position) + ".\n")
        count += 1
        position = text.find(key,position+1)
    outfile.write(key + " is found " + str(count) + " time(s).\n")
    outfile.close()
    infile.close()
    print("Done")

# # Test code
# find_all_count('article.txt','computer')     # 6 time(s).
# find_all_count('article.txt','Whole Earth')  # 2 time(s).
# find_all_count('article.txt','Apple')        # 9 time(s).
# find_all_count('article.txt','commencement') # 1 time(s).
# find_all_count('article.txt','apple')        # 0 time(s).

### 실습 6.7 - 인용 문장 모두 찾기 (p.305)

def find_quotes_all(filename):
    infile = open(filename,"r")
    outfile = open(filename+"-out.txt","w")
    text = infile.read()
    count = 0
    quote_begin = text.find('"')
    while quote_begin != -1:
        quote_end = text.find('"', quote_begin+1)
        count += 1
        outfile.write(text[quote_begin:quote_end+1] + "\n\n")
        quote_begin = text.find('"',quote_end+1)
    outfile.write("There are " + str(count) + " quotes in total.\n")
    outfile.close()
    infile.close()
    print("Done")

# # Test code
# find_quotes_all("article.txt")



#### 연습문제

### 6.1 - 정수 리스트에서 가장 큰 수 찾기 (p.306)

# code : 6-20.py
def greatest(ns):
    def loop(ns,top):
        if ns != []:
            if ns[0] > top:
                return loop(ns[1:],ns[0])
            else:
                return loop(ns[1:],top)
        else:
            return top
    if len(ns) == 0:
        return None
    else:
        return loop(ns[1:],ns[0])

def greatest(ns):
    if len(ns) == 0:
        return None
    else:
    	top = ns[0]
    	ns = ns[1:]
    	while ns != []:
    		if ns[0] > top:
    			top = ns[0]
    		ns = ns[1:]
    	return top

def greatest(ns):
    if len(ns) == 0:
        return None
    else:
    	top = ns[0]
    	for n in ns:
    		if n > top:
    			top = n
    	return top

# # Test code
# print(greatest([5,2,3,6,4,3,7,5,8,2])) # 8
# print(greatest([5,2]))                 # 5
# print(greatest([5]))                   # 5
# print(greatest([]))                    # None

### 6.2 - 정수 리스트에서 i번째 큰 수 찾기 (p.307)

# code : 6-21.py
def rankith(ns,i):
    if  i <= 0 or len(ns) < i:
        return None
    else:
        while i > 0:
            largest = max(ns)
            ns.remove(largest)
            i = i - 1
        return largest

# # Test code
# print(rankith([5,2,3,6,4,3,7,5,8,2],1)) # 8
# print(rankith([5,2,3,6,4,3,7,5,8,2],2)) # 7
# print(rankith([5,2,3,6,4,3,7,5,8,2],4)) # 5
# print(rankith([5,2,3,6,4,3,7,5,8,2],5)) # 5
# print(rankith([5,2,3,6,4,3,7,5,8,2],6)) # 4
# print(rankith([5,2],2))                 # 2
# print(rankith([5],1))                   # 5
# print(rankith([],1))                    # None

### 6.3 - 문자열에서 특정 문자 모두 없애기 (p.307-308)

# code : 6-22.py
def remove(x,xs):
    if xs != "":
        if x != xs[0]:
            return xs[0] + remove(x,xs[1:])
        else:
            return remove(x,xs[1:])
    else:
        return ""

# # Test code
# print(remove('z','')) # ''
# print(remove('a','abracadabra')) # 'brcdbr'
# print(remove('z','abracadabra')) # 'abracadabra'


# 꼬리재귀 함수 버전
def remove(x,xs):
    def loop(xs,rs):
        if xs != "":
            if x != xs[0]:
                return loop(xs[1:],rs+xs[0])
            else:
                return loop(xs[1:],rs)
        else:
            return rs
    return loop(xs,"")

# # Test code
# print(remove('z','')) # ''
# print(remove('a','abracadabra')) # 'brcdbr'
# print(remove('z','abracadabra')) # 'abracadabra'

# while 루프 함수 버전
def remove(x,xs):
    rs = ""
    while xs != "":
        if x != xs[0]:
            rs = rs + xs[0]
        xs = xs[1:]
    return rs

# # Test code
# print(remove('z','')) # ''
# print(remove('a','abracadabra')) # 'brcdbr'
# print(remove('z','abracadabra')) # 'abracadabra'

# for 루프 함수 버전
def remove(x,xs):
    rs = ""
    for y in xs:
        if x != y:
            rs = rs + y
    return rs

# # Test code
# print(remove('z','')) # ''
# print(remove('a','abracadabra')) # 'brcdbr'
# print(remove('z','abracadabra')) # 'abracadabra'


### 6.4 - 중복 골라내기 (p.308)
### 문자열 인수를 받아서 2번 이상 나온 문자만 나열한 리스트를 내주는 함수

# code : 6-23.py
def collect_dups(s):
    singles = ""
    duplicates = []
    for c in s:
        if c not in singles:
            singles += c
        elif c not in duplicates:
            duplicates.append(c)
    return duplicates

# # Test code
# print(collect_dups("sophisticated"))
#                  # ['s', 'i', 't']
# print(collect_dups("I'm no angel."))
#                  # [' ', 'n']
# print(collect_dups("Stay Hungry. Stay Foolish."))
#                  # ['y', ' ', 'S', 't', 'a', 'o', '.']
# print(collect_dups("Your time is limited, so don’t waste it living someone else’s life."))
#                  # [' ', 'i', 'm', 't', 'e', 's', 'o', 'd', 'l', 'n', '’']


### 6.5 - 아이소그램 확인 (p.309)

def isisogram(word):
    while word != '' and word[1:] != '':
        if word[0] in word[1:]:
            return False
        else:
            word = word[1:]
    return True

# # Test code
# print(isisogram(""))                 # True
# print(isisogram("a"))                # True
# print(isisogram("aa"))               # False
# print(isisogram("and"))              # True
# print(isisogram("hanyang"))          # False
# print(isisogram("playground"))       # True
# print(isisogram("uncopyrightables")) # True


### 6.6 - 아나그램 확인 (p.309-310)
# sort() 함수 사용 자제

# code : 6-24.py
def isanagram(word1,word2):
    while word1 != '':
        if word1[0] in word2:
            index = word2.find(word1[0])
            word1 = word1[1:]
            word2 = word2[:index] + word2[index+1:]
        else:
            return False
    return word2 == ''
            
# # Test code
# print(isanagram('',''))                 # True
# print(isanagram('z','z'))               # True
# print(isanagram('zz','z'))              # False
# print(isanagram('z','zz'))              # False
# print(isanagram('silent','listen'))     # True
# print(isanagram('silent','listens'))    # False
# print(isanagram('elvis','lives'))       # True
# print(isanagram('restful','fluster'))   # True
# print(isanagram('restfully','fluster')) # False
# print(isanagram('문전박대','대박전문'))      # True



### 6.7 - 완전수 찾기 (p.310)

# 자산을 제외한 약수의 리스트를 모아주는 보조 함수
def collect_divisors(n):
    divisor = 2
    divisors = [1]
    while n / divisor >= 2:
        if n / divisor == n // divisor:
            divisors.append(divisor)
        divisor += 1
    return divisors

# # Test code
# print(collect_divisors(6)) # [1, 2, 3]
# print(collect_divisors(28)) # [1, 2, 4, 7, 14]
# print(collect_divisors(29)) # [1]

def find_perfects_upto(n):
    perfects = []
    for i in range(2,n+1):
        total = sum(collect_divisors(i))
        if i == total:
            perfects.append(i)
    return perfects

# # Test code
# print(find_perfects_upto(30)) # [6, 28]
# print(find_perfects_upto(10000)) # [6, 28, 496, 8128]


### 6.8 - 정렬된 리스트에서 가장 넓은 간격 찾기 (p.311)

# code : 6-25.py
def search_widest_gap(ss):
    # assume that ss is sorted
    if len(ss) == 0:
        return None, 0
    elif len(ss) == 1:
        return 0, 0
    else: # len(ss) >= 2
        widest = 0
        index = 0
        for i in range(len(ss)-1):
            gap = ss[i+1] - ss[i] # always >= 0
            if gap > widest:
                widest = gap
                index = i
        return index, widest

# # Test code
# print(search_widest_gap([]))                     # (None, 0)
# print(search_widest_gap([3]))                    # (0, 0)
# print(search_widest_gap([3,5,8,20,22]))          # (2, 12)
# print(search_widest_gap([3,5,8,20,22,34,37,40])) # (2, 12)

# code : 6-26.py
import random
def test_search_widest_gap():
    db = random.sample(range(500),100)
    print("Searching the widest gap...")
    db.sort()
    print(db)
    index, gap = search_widest_gap(db)
    print("The widest gap is:", gap)
    print("between", db[index], "and", db[index+1])
    print("at", index)
    
# # Test code
# test_search_widest_gap()


### 6.9 - 오르막 리스트 (p.312-315)

## 가. ascending 함수

# code : 6-27.py
def ascending(ns):
    if len(ns) <= 1:
        return False
    else:
        front = ns[0]
        for n in ns[1:]:
            if front >= n:
                return False
            front = n
        return True

# # Test code
# print(ascending([1,3]))                # True
# print(ascending([2, 3, 6, 8, 12, 17])) # True
# print(ascending([]))                   # False
# print(ascending([2]))                  # False
# print(ascending([3, 3, 3, 3, 3]))      # False
# print(ascending([1, 2, 2, 3]))         # False
# print(ascending([2, 3, 1]))            # False

## 나. sublists 함수

# code : 6-28.py
def sublists(ns):
    def get(k,ns):
        subs = []
        for i in range(len(ns)-k+1):
            subs.append(ns[i:i+k])
        return subs
    subs = [[]]
    for k in range(1,len(ns)):
        subs += get(k,ns)
    if ns != []:
        subs.append(ns)
    return subs

# # Test code
# print(sublists([])) 
# # [[]]
# print(sublists([1])) 
# # [[], [1]]
# print(sublists([1,2])) 
# # [[], [1], [2], [1, 2]]
# print(sublists([1,2,3])) 
# # [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
# print(sublists([1,2,3,4])) 
# # [[], [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]

## 다. ascending_sublists 함수

# code : 6-29.py
def ascending_sublists(ns):
    ascs = []
    for sub in sublists(ns):
        if ascending(sub):
            ascs.append(sub)
    return ascs

# # Test code
# print(ascending_sublists([])) 
# # []
# print(ascending_sublists([1])) 
# # []
# print(ascending_sublists([1,2])) 
# # [[1, 2]]
# print(ascending_sublists([1,2,3])) 
# # [[1, 2], [2, 3], [1, 2, 3]]
# print(ascending_sublists([3,1,2])) 
# # [[1, 2]]
# print(ascending_sublists([1,3,2])) 
# # [[1, 3]]
# print(ascending_sublists([1,5,3,4,8,2,3,5])) 
# # [[1, 5], [3, 4], [4, 8], [2, 3], [3, 5], [3, 4, 8], [2, 3, 5]]

## 라. longest_ascending_sublist 함수

# code : 6-30.py
# stand-alone version
def longest_ascending_sublist(ns):
	if ns != []:
		longest = []
		current = [ns[0]]
		for n in ns[1:]:
			if current[-1] < n:
				current.append(n)
			else:
				if len(longest) < len(current):
					longest = current
				current = [n]
		return longest
	else:
		return []

# the version calling ascending_sublists
def longest_ascending_sublist(ns):
    ascs = ascending_sublists(ns)
    if ascs != []:
        index = len(ascs) - 1
        while index != 0 and len(ascs[index]) == len(ascs[index-1]):
            index -= 1
        return ascs[index]
    else:
        return []

# # Test code
# print(longest_ascending_sublist([1,5,3,4,8,2,3,5]))
# # [3, 4, 8]
# print(longest_ascending_sublist([]))
# # []
# sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63, 98, 59, 7, 23, 34, 67, 77, 30, 49, 55, 31, 58, 10, 27, 15, 45, 42, 77, 11, 14, 9, 55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
# print(longest_ascending_sublist(sample))
# # [28, 37, 61, 66, 89]


## 마. longest_steepest_ascending_sublist 함수

# code : 6-31.py
# stand-alone version
def longest_steepest_ascending_sublist(ns):
	def slope(ns):
		return (ns[-1] - ns[0]) / len(ns)
	if ns != []:
		longest = []
		steepest = 0
		current = [ns[0]]
		for n in ns[1:]:
			if current[-1] < n:
				current.append(n)
			else:
				if len(longest) < len(current):
					longest = current
					steepest = slope(longest)
				elif len(longest) == len(current) and steepest < slope(current):
					longest = current
					steepest = slope(current)
				current = [n]
		return longest
	else:
		return []

# the version calling ascending_sublists
def longest_steepest_ascending_sublist(ns):
    ascs = ascending_sublists(ns)
    if ascs != []:
        index = len(ascs) - 1
        steepest = ascs[index]
        while index > 0 and len(ascs[index]) == len(ascs[index-1]):
            if steepest[-1] - steepest[0] <= ascs[index-1][-1] - ascs[index-1][0]:
                steepest = ascs[index-1]
            index -= 1
        return steepest
    else:
        return []

# # Test code
# print(longest_steepest_ascending_sublist([1,5,3,4,8,2,3,5]))
# # [3, 4, 8]
# print(longest_steepest_ascending_sublist([]))
# # []
# sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63, 98, 59, 7, 23, 34, 67, 77, 30, 49, 55, 31, 58, 10, 27, 15, 45, 42, 77, 11, 14, 9, 55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
# print(longest_steepest_ascending_sublist(sample))
# # [7, 23, 34, 67, 77]


### 6.10 - 가장 긴 스트릭 (p.315-318)

# code : 6-32.py
def longest_streak(s):
    if s != '':
        contender = leader = s[0]
        streak_length = streak_record = 1 
        for n in s[1:]:
            if n == contender:
                streak_length = streak_length + 1
            else:
                contender = n
                streak_length = 1
            if streak_length > streak_record:
                leader = contender
                streak_record = streak_length
        return leader, streak_record
    else:
        return None

# # Test code
# print(longest_streak(""))
# # None
# print(longest_streak("5"))
# # ('5', 1)
# print(longest_streak("06479019955907200041185008780528384811265678111671"))
# # ('0', 3)
# print(longest_streak("49715114250863455559013207228395154984882560834674")) 
# # ('5', 4)
# print(longest_streak("79083787262159815638834042282485195270836937488097")) 
# # ('8', 2)
# print(longest_streak("36888653851748777011129000999371447120618209984726"))
# # ('8', 3)

## 가. longest_streak1 함수

# code : 6-33.py
def longest_streak1(s):
    if s != '':
        contender = leader = s[0]
        streak_length = streak_record = 1
        contender_index = leader_index = 0
        index = 1
        for n in s[1:]:
            if n == contender:
                streak_length += 1
            else:
                contender = n
                streak_length = 1
                contender_index = index
            if streak_length > streak_record:
                leader = contender
                streak_record = streak_length
                leader_index = contender_index
            index += 1
        return leader, streak_record, leader_index
    else:
        return None

# # Test code
# print(longest_streak1(""))
# # None
# print(longest_streak1("5"))
# # ('5', 1, 0)
# print(longest_streak1("06479019955907200041185008780528384811265678111671"))
# # ('0', 3, 15)
# print(longest_streak1("49715114250863455559013207228395154984882560834674")) 
# # ('5', 4, 15)
# print(longest_streak1("79083787262159815638834042282485195270836937488097")) 
# # ('8', 2, 19)
# print(longest_streak1("36888653851748777011129000999371447120618209984726"))
# # ('8', 3, 2)

## 나. longest_streak2 함수

# code : 6-34.py
def longest_streak2(s):
    if s != '':
        contender = leader = s[0]
        streak_length = streak_record = 1
        contender_index = leader_index = 0
        ties = []
        index = 1
        for n in s[1:]:
            if n == contender:
                streak_length += 1
            else:
                contender = n
                streak_length = 1
                contender_index = index
            if streak_length > streak_record:
                leader = contender
                streak_record = streak_length
                leader_index = contender_index
                ties = []
            elif streak_length == streak_record:
                coleader = (contender, streak_length, contender_index)
                ties.append(coleader)
            index += 1
        return [(leader, streak_record, leader_index)] + ties
    else:
        return []

# # Test code
# print(longest_streak2(""))
# # []
# print(longest_streak2("5"))
# # [('5', 1, 0)]
# print(longest_streak2("06479019955907200041185008780528384811265678111671"))
# # [('0', 3, 15), ('1', 3, 44)]
# print(longest_streak2("49715114250863455559013207228395154984882560834674")) 
# # [('5', 4, 15)]
# print(longest_streak2("79083787262159815638834042282485195270836937488097")) 
# # [('8', 2, 19), ('2', 2, 25), ('8', 2, 45)]
# print(longest_streak2("36888653851748777011129000999371447120618209984726"))
# # [('8', 3, 2), ('7', 3, 14), ('1', 3, 18), ('0', 3, 23), ('9', 3, 26)]


### 6.11 - 소수하고 나~하고 (p.318-321)

# code : 6-35.py
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

# # Test code
# for i in range(50):
#   if is_prime(i):
#       print(i)

## 가. is_prime 함수 (효율 개선)

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3,n,2):
            if n % i == 0:
                return False
        return True

# # Test code
# for i in range(50):
#     if is_prime(i):
#         print(i)

## 나. all_primes_less_than 함수

# code : 6-36.py
def all_primes_less_than(n):
    p = []
    for i in range(n):
        if is_prime(i):
            p.append(i)
    return p

# # Test code
# print(all_primes_less_than(2)) # []
# print(all_primes_less_than(3)) # [2]
# print(all_primes_less_than(5)) # [2, 3]
# print(all_primes_less_than(10)) # [2, 3, 5, 7]
# print(all_primes_less_than(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
# print(all_primes_less_than(30)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

## 다. primes 함수

# code : 6-37.py
def primes(k):
    p = []
    n = 2
    while k > 0:
        if is_prime(n):
            p.append(n)
            k -= 1
        n += 1
    return p

# # Test code
# print(primes(0)) # []
# print(primes(1)) # [2]
# print(primes(5)) # [2, 3, 5, 7, 11]
# print(primes(10)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

## 라. twin_primes 함수 - 쌍둥이 소수 k 쌍 찾기 (차이가 2인 소수의 쌍)

# code : 6-38.py
def twin_primes(k):
    p = []
    prev = 2
    n = 3
    while k > 0:
        if is_prime(n):
            if n - 2 == prev:
                twin = (prev, n)
                p.append(twin)
                k -= 1
            prev = n
        n += 2
    return p

# # Test code
# print(twin_primes(0)) # []
# print(twin_primes(1)) # [(3, 5)]
# print(twin_primes(5)) 
# # [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31)]
# print(twin_primes(10)) 
# # [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73), (101, 103), (107, 109)]



### 6.12 - 가장 가까운 키 이분검색 (p.321-324)

# code : 6-40.py
def bin_search_closest(ss,x):
    if ss == []:
        return None
    low = 0
    high = highest = len(ss) - 1
    while low <= high:
        mid = (high + low) // 2
        if x == ss[mid]:
            return mid
        elif x < ss[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if high < 0:
        high = 0
    if low > highest:
        low = highest
    diffLow = abs(x - ss[low])
    diffHigh = abs(x - ss[high])
    if diffLow < diffHigh:
        return low
    else:
        return high

# # Test code
# print(bin_search_closest([],3))            # None
# print(bin_search_closest([8],5))           # 0
# print(bin_search_closest([8],8))           # 0
# print(bin_search_closest([8],9))           # 0
# print(bin_search_closest([1,2,5,9,10],0))  # 0
# print(bin_search_closest([1,2,5,9,10],1))  # 0
# print(bin_search_closest([1,2,5,9,10],2))  # 1
# print(bin_search_closest([1,2,5,9,10],3))  # 1
# print(bin_search_closest([1,2,5,9,10],4))  # 2
# print(bin_search_closest([1,2,5,9,10],5))  # 2
# print(bin_search_closest([1,2,5,9,10],6))  # 2
# print(bin_search_closest([1,2,5,9,10],7))  # 2
# print(bin_search_closest([1,2,5,9,10],8))  # 3
# print(bin_search_closest([1,2,5,9,10],9))  # 3
# print(bin_search_closest([1,2,5,9,10],10)) # 4
# print(bin_search_closest([1,2,5,9,10],11)) # 4

# code : 6-41.py
import random
def test_bin_search_closest():
    data = random.sample(range(500),100)
    print("Binary search closest function test")
    data.sort()
    print(data)
    for _ in range(10):
        x = random.randrange(500)
        index = bin_search_closest(data, x)
        print("The closest value to", x, ":", data[index], "at index", index)

# # Test code
# test_bin_search_closest()




        