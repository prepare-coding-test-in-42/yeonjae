from collections import deque
from itertools import combinations

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def in_bounds(x: int, y: int, N: int) -> bool:
    return 0 <= x < N and 0 <= y < N


def bfs(comb, board, num_of_blanks):
    N = len(board)
    queue = deque(comb)
    visited = [[-1] * N for _ in range(N)]

    for r, c in comb:
        queue.append((r, c))
        visited[r][c] = 0
    
    infectee = 0

    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc, N) or visited[nr][nc] != -1 or board[nr][nc] == 1:
                continue
            visited[nr][nc] = visited[r][c] + 1
            queue.append((nr, nc))
            if board[nr][nc] == 0:
                infectee += 1
        
    if infectee != num_of_blanks:
        return float('inf')
    
    max_time = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                max_time = max(max_time, visited[r][c])
    
    return max_time


def main():
    N, M = map(int, input().split())
    viruses = []
    board = []
    num_of_blanks = 0

    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 2:
                viruses.append((r, c))
            elif row[c] == 0:
                num_of_blanks += 1
        board.append(row)
    
    combs = combinations(viruses, M)
    
    answer = float('inf')
    for comb in combs:
        time = bfs(comb, board, num_of_blanks)
        answer = min(answer, time)
    
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)
    

if __name__ == "__main__":
    main()