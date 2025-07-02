N, M = map(int, input().split())
mars = []

for _ in range(N):
    mars.append(list(map(int, input().split())))

dp = [[0] * M for _ in range(N)]
dp[0][0] = mars[0][0]
for col in range(1, M):
    dp[0][col] = dp[0][col - 1] + mars[0][col]

for row in range(1, N):
    temp_left = [0] * M
    temp_right = [0] * M

    temp_left[0] = dp[row - 1][0] + mars[row][0]
    for col in range(1, M):
        temp_left[col] = max(temp_left[col - 1], dp[row - 1][col]) + mars[row][col]

    temp_right[M - 1] = dp[row - 1][M - 1] + mars[row][M - 1]
    for col in range(M - 2, -1, -1):
        temp_right[col] = max(temp_right[col + 1], dp[row - 1][col]) + mars[row][col]

    for col in range(M):
        dp[row][col] = max(temp_left[col], temp_right[col])
    
print(dp[N - 1][M - 1])