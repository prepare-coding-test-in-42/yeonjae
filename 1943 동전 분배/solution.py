for _ in range(3):
    N = int(input())

    wallet = []
    total_num = 0
    total_sum = 0
    for _ in range(N):
        coin, num = map(int, input().split())
        total_num += num
        total_sum += coin * num
        wallet.append((coin, num))
    
    # 동전의 금액 총합이 홀수이면
    if total_sum % 2 != 0:
        print(0)
        continue
    
    target = total_sum // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for coin, num in wallet:
        count = num
        k = 1
        while count > 0:
            use = min(k, count)
            cost = coin * use
            for i in range(target, cost - 1, -1):
                if dp[i - cost]:
                    dp[i] = True
            count -= use
            k *= 2
    
    print(1 if dp[target] else 0)