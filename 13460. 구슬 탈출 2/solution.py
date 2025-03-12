import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = []

for i in range(N):
    row = list(input().rstrip())
    for j, cell in enumerate(row):
        if cell == 'R':
            Rx, Ry = i, j
            row[j] = '.'
        elif cell == 'B':
            Bx, By = i, j
            row[j] = '.'
        # elif cell == 'O':
        #     Ox, Oy = i, j
    board.append(row)


def move(x, y, dx, dy):
    # 이동 중 구멍에 빠졌는지 확인하기 위한 flag
    flag = False
    # 벽이나 구멍이 아닐 때 계속 이동
    count = 0
    while board[x + dx][y + dy] != '#':
        x += dx
        y += dy
        count += 1
        # 구멍에 빠지면 flag 활성화
        if board[x][y] == 'O':
            flag = True
            break
    return x, y, count, flag


def bfs():
    # 큐 초기화
    queue = deque()
    # 구슬 위치와 이동 횟수 저장
    queue.append((Rx, Ry, Bx, By, 0))
    visited = set()
    visited.add((Rx, Ry, Bx, By))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        # 이동 횟수가 10 이상이면 실패
        if depth >= 10:
            return -1
        
        # 네 방향으로 구슬을 굴려보기
        for dx, dy in directions:
            # 빨간 구슬 이동
            new_rx, new_ry, r_count, r_is_in_hole = move(rx, ry, dx, dy)
            # 파란 구슬 이동
            new_bx, new_by, b_count, b_is_in_hole = move(bx, by, dx, dy)
            
            # 파란 구슬이 구멍에 빠지면 실패
            if b_is_in_hole:
                continue

            # 빨간 구슬만 구멍에 빠지면 성공
            if r_is_in_hole:
                return depth + 1
            
            # 두 구슬이 겹치는 경우
            if new_rx == new_bx and new_ry == new_by:
                if r_count > b_count:
                    new_rx -= dx
                    new_ry -= dy
                else:
                    new_bx -= dx
                    new_by -= dy
            
            # 방문 체크 후 큐에 추가
            if (new_rx, new_ry, new_bx, new_by) not in visited:
                visited.add((new_rx, new_ry, new_bx, new_by))
                queue.append((new_rx, new_ry, new_bx, new_by, depth + 1))

    return -1


# 🛠 진입점 설정
if __name__ == "__main__":
    result = bfs()
    print(result)