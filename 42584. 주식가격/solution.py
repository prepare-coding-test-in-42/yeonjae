def solution(prices):
    answer = []
    for i in range(len(prices)):
        duration = 0
        for j in range(i + 1, len(prices)):
            duration += 1
            # if prices[j] < prices[i] and j == i + 1:
            #     duration = 1
            #     break
            if prices[j] < prices[i]:
                break
        answer.append(duration)
    return answer