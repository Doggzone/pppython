def longest_streak(s):
    if s != '':
        contender = leader = s[0]
        streak_length = streak_record = 1
        for n in s[1:]:
            if n == contender:
                streak_length += 1
            else:
                contender = n
                streak_length = 1
            if streak_length > streak_record:
                leader = contender
                streak_record = streak_length
        return leader, streak_record
    else:
        return None

# Test code
print(longest_streak(""))  # None
print(longest_streak("5")) # ('5', 1)
print(longest_streak("06479019955907200041185008780528384811265678111671")) # ('0', 3)
print(longest_streak("49715114250863455559013207228395154984882560834674")) # ('5', 4)
print(longest_streak("79083787262159815638834042282485195270836937488097")) # ('8', 2)
print(longest_streak("36888653851748777011129000999371447120618209984726")) # ('8', 3)