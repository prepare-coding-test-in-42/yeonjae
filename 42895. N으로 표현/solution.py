def calculate(first, second):
    result = set()
    
    for f in first:
        for s in second:
            result.add(f + s)
            result.add(f - s)
            result.add(f * s)
            if s != 0:
                result.add(f // s)

    return result


def solution(N, number):
    if (number == N):
        return 1
    
    dp = [set() for _ in range(8)]

    dp[0].add(N)
    for i in range(1, 8):
        # N을 (i + 1)번 반복한 숫자 추가
        dp[i].add(int(str(N) * (i + 1)))

        for j in range(i):
            dp[i].update(calculate(dp[j], dp[i - j - 1]))
        
        if number in dp[i]:
            return i + 1
        
    return -1
