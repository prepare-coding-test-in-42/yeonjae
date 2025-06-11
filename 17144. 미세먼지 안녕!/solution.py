from copy import deepcopy

R, C, T = map(int, input().split())
board = []
purifiers = []
dusts = []


for r in range(R):
    row = list(map(int, input().split()))
    for c in range(C):
        if row[c] == -1:
            purifiers.append((r, c))
        elif row[c] > 0:
            dusts.append((r, c))
    board.append(row)


def spread(row, col, temp):
    amount = board[row][col] // 5
    if amount == 0:
        return
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 퍼진 방향 수
    count = 0

    for idx in range(4):
        nr = row + dr[idx]
        nc = col + dc[idx]

        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
            temp[nr][nc] += amount
            count += 1
    
    # 현재 위치에서 퍼진 양만큼 감소
    temp[row][col] -= amount * count


def purify():
    global board

    temp = deepcopy(board)

    # 순환 방향 구분을 위한 공기청정기 위치 저장
    top, bottom = purifiers[0][0], purifiers[1][0]

    # 위쪽 순환 (반시계 방향)
    # 1. 아래로 (공기청정기 위쪽 열 아래로 밀기)
    for r in range(top - 1, 0, -1):
        temp[r][0] = board[r - 1][0]
    
    # 2. 왼쪽으로 (맨 윗줄 왼쪽 이동)
    for c in range(C - 1):
        temp[0][c] = board[0][c + 1]
    
    # 3. 위로
    for r in range(top):
        temp[r][C - 1] = board[r + 1][C - 1]

    # 4. 오른쪽으로
    for c in range(2, C):
        temp[top][c] = board[top][c - 1]

    temp[top][1] = 0

    # 아래쪽 순환

    # 1. 위로 (공기청정기 위쪽 열 위로 밀기)
    for r in range(R - 1, bottom + 1, -1):
        temp[r - 1][0] = board[r][0]
    
    # 2. 왼쪽으로
    for c in range(C - 1):
        temp[R - 1][c] = board[R - 1][c + 1]
    
    # 3. 아래로
    for r in range(bottom + 1, R):
        temp[r][C - 1] = board[r - 1][C - 1]
    
    # 4. 오른쪽으로
    for c in range(2, C):
        temp[bottom][c] = board[bottom][c - 1]

    temp[bottom][1] = 0

    # 공기청정기 위치 저장
    temp[top][0] = -1
    temp[bottom][0] = -1

    board = temp


def solution():
    global board, dusts

    for _ in range(T):
        # 임시 맵 생성
        temp = deepcopy(board)

        # 미세먼지 확산
        for r, c in dusts:
            spread(r, c, temp)

        # 확산 결과로 원래 맵 갱신
        board = temp

        # 공기청정기 작동
        purify()
        
        # dusts 갱신
        new_dusts = []
        for r in range(R):
            for c in range(C):
                if board[r][c] > 0:
                    new_dusts.append((r, c))

        dusts = new_dusts
    
    total = 0

    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                total += board[r][c]
    
    return total


if __name__ == "__main__":
    print(solution())
