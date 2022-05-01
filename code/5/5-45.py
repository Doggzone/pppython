def substrings_of_length(k,s):
    if k == 0:
        return ['']
    elif 0 < k <= len(s):
        subs = []
        pass  # Write your for-loop code here.
        return subs
    else:
        return None

# Test code
print(substrings_of_length(0,"ERICA")) # ['']
print(substrings_of_length(1,"ERICA")) # ['E', 'R', 'I', 'C', 'A']
print(substrings_of_length(2,"ERICA")) # ['ER', 'RI', 'IC', 'CA']
print(substrings_of_length(3,"ERICA")) # ['ERI', 'RIC', 'ICA']
print(substrings_of_length(4,"ERICA")) # ['ERIC', 'RICA']
print(substrings_of_length(5,"ERICA")) # ['ERICA']
print(substrings_of_length(6,"ERICA")) # None