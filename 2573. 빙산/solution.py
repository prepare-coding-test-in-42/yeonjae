import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 , 1]

def in_bounds(x, y, N):
    return 0 <= x < N and 0 <= y < M


def bfs(x, y, visited):
    # queue = deque((x, y))
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not in_bounds(nx, ny, N):
                continue
            if not visited[nx][ny] and board[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))


def melt():
    # amounts = [[0] * M for _ in range(N)]
    amounts = []

    for x in range(N):
        for y in range(M):
            if board[x][y] > 0:
                count = 0
                for idx in range(4):
                    nx, ny = x + dx[idx], y + dy[idx]
                    if in_bounds(nx, ny, N) and board[nx][ny] == 0:
                        # amount[x][y] += 1
                        count += 1
                if count > 0:
                    amounts.append((x, y, count))

    # for x in range(N):
    #     for y in range(M):
    #         board[x][y] = max(0, board[x][y] - amount[x][y])
    for x, y, count in amounts:
        board[x][y] = max(0, board[x][y] - count)


year = 0
while True:
    visited = [[False] * M for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1
    
    if count == 0:
        print(0)
        break
    elif count >= 2:
        print(year)
        break

    melt()
    year += 1