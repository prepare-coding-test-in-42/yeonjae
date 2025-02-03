def solution(clothes):
    answer = 1

    closet = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in closet:
            closet[clothes[i][1]] = 0
        closet[clothes[i][1]] += 1
    
    for item in closet:
        answer *= closet[item] + 1
        
    return answer - 1