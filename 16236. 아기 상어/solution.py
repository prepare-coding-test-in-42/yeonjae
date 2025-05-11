from collections import deque

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def in_bounds(x: int, y: int, N: int) -> bool:
    return 0 <= x < N and 0 <= y < N


def bfs(x, y, size, board):
    N = len(board)
    queue = deque([(0, x, y)])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    fishes = []

    while queue:
        dist, x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not in_bounds(nx, ny, N) or visited[nx][ny] or board[nx][ny] > size:
                continue
            visited[nx][ny] = True
            if 0 < board[nx][ny] < size:
                fishes.append((dist + 1, nx, ny))
            queue.append((dist + 1, nx, ny))
    
    return min(fishes, key=lambda x: (x[0], x[1], x[2])) if fishes else None


def main():
    N = int(input())
    board = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 9:
                shark_x, shark_y = r, c
                row[c] = 0
        board.append(row)
    
    size = 2
    cnt = 0
    time = 0

    while True:
        result = bfs(shark_x, shark_y, size, board)
        if result is None:
            break
        dist, x, y = result
        time += dist
        shark_x, shark_y = x, y
        board[x][y] = 0
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0

    print(time)


if __name__ == "__main__":
    main()