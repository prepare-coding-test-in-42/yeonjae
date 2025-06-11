from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(x, y, color, visited):
    global board

    queue = deque()
    queue.append((x, y))
    group = [(x, y)]
    rainbow = []
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            if not in_bounds(nx, ny) or visited[nx][ny] or board[nx][ny] == -1:
                continue
            # 일반 블록 같은 색 or 무지개 블록이면 group에 포함
            if board[nx][ny] == 0:
                rainbow.append((nx, ny))
            visited[nx][ny] = True
            group.append((nx, ny))
            queue.append((nx, ny))

    # 방문 처리 복원
    for rx, ry in rainbow:
        visited[rx][ry] = False

    return group, len(rainbow), (x, y)


def find_largest_group():
    # 모든 칸을 돌면서 블록 그룹들을 BFS로 탐색하고, 조건에 맞는 최적 그룹 반환
    visited = [[False] * N for _ in range(N)]
    best = []

    for i in range(N):
        for j in range(N):
            # 일반 블록만 시작점
            if board[i][j] > 0 and not visited[i][j]:
                group, rainbow_count, std_block = bfs(i, j, board[i][j], visited)
                if len(group) >= 2:
                    if [group, rainbow_count, -std_block] > best:
                        best = [group, rainbow_count, -std_block]
    return best


def remove_group(group):
    for x, y in group:
        board[x][y] = -2


def apply_gravity():
    global board

    for j in range(N):
        for i in range(N -2, -1, -1):
            # 중력의 영향을 받는 블록(무지개 블록, 일반 블록)인 경우
            if board[i][j] >= 0:
                while True:
                    r = i
                    if r + 1 < N and board[r + 1][j] == -2:
                        board[r][j], board[r + 1][j] = -2, board[r][j]
                    else:
                        break


def rotate_board():
    new_board = []
    for i in range(N):
        new_row = []
        for j in range(N):
            new_row.append(board[j][N - 1 - i])
        new_board.append(new_row)
    return new_board


def main():
    score = 0
    global board

    while True:
        group = find_largest_group()
        if not group:
            break
        remove_group(group)
        score += len(group) ** 2
        apply_gravity()
        board = rotate_board()
        apply_gravity()
    print(score)


if __name__ == "__main__":
    main()
