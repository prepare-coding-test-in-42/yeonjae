from itertools import product

def solution(word):
    strs = []
    for length in range(1, 6):
        for prod in product('AEIOU', repeat=length):
            strs.append(''.join(prod))
    
    strs.sort()

    for idx in range(len(strs)):
        if word == strs[idx]:
            return idx + 1
        continue

