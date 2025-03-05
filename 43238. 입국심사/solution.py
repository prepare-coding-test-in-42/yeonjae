def solution(n, times):
    start = 1
    end = max(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for time in times:
            count += mid // time
        if count >= n:
            end = mid - 1
        else:
            start = mid + 1
    return start