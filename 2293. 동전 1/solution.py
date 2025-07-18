n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k + 1)
# 0원을 만드는 방법 한 가지
dp[0] = 1

for coin in coins:
    for amount in range(coin, k + 1):
        # dp[amount]는 amount원을 만드는 방법의 수
        dp[amount] += dp[amount - coin]

print(dp[k])