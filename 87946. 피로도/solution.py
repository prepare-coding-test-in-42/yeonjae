from itertools import permutations

def solution(k, dungeons):
    # sorted_dungeons = sorted(dungeons, key=lambda x : x[0], reverse=True)
    perms = permutations(dungeons, len(dungeons))

    max_dungeons = 0
    for perm in perms:
        curr_fatigue = k
        count = 0
        for min_fatigue, cost in perm:
            if curr_fatigue >= min_fatigue:
                curr_fatigue -= cost
                count += 1
            else:
                break
        max_dungeons = max(max_dungeons, count)
            
    return max_dungeons

