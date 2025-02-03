def solution(answers):
    results = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    honors = []
    scores = {}
    for i in range(len(results)):
        score = 0
        for j in range(len(answers)):
            if answers[j] == results[i][j % len(results[i])]:
                score += 1
        scores[i] = score
    
    acme = max(scores.values())
    for key in scores:
        if scores[key] == acme:
            honors.append(key + 1)

    honors.sort()

    return honors

