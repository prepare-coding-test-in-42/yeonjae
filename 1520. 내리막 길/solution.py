import sys
sys.setrecursionlimit(10**6)

# 현재 칸 (x, y)에서 가능한 방향은 상하좌우 중 나보다 높이가 높은 칸에서 오는 경로의 수들의 총합
M, N = map(int, input().split())

board = []
for _ in range(M):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[-1] * N for _ in range(M)]

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < M

# dfs(x, y)는 (x, y)에서 도착지까지 갈 수 있는 경로의 수
def dfs(x, y):
    # 도착한 경우
    if (x, y) == (N - 1, M - 1):
        return 1
    # 이미 계산된 경우
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny) and board[ny][nx] < board[y][x]:
            dp[y][x] += dfs(nx, ny)
    
    return dp[y][x]

print(dfs(0, 0))