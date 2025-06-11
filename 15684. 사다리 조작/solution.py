N, M, H = map(int, input().split())
ladder = [[0] * (N + 1) for _ in range(H + 1)]
flag = False

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1

def check_ladder():
    for start in range(1, N + 1):
        # 현재 위치
        col = start
        for row in range(1, H + 1):
            # 현재 위치에서 오른쪽으로 연결된 경우
            if col < N and ladder[row][col] == 1:
                col += 1
            # 현재 위치에서 왼쪽으로 연결된 경우
            elif col > 1 and ladder[row][col - 1] == 1:
                col -= 1
        
        # 도착 지점이 시작 지점과 다르면 실패
        if col != start:
            return False
    
    return True


def put_ladders(count, depth, x, y):
    global flag
    
    if depth == count:
        if check_ladder():
            flag = True
        return

    for row in range(x, H + 1):
        # 사다리를 col에서 col + 1로 놓는 구조라서 col == N일 때는 col + 1이 범위를 넘어서 버림
        for col in range(y, N):
            # 해당 위치에 사다리를 놓을 수 없는 경우
            if ladder[row][col] == 1:
                continue
            if ladder[row][col - 1] == 1:
                continue
            if ladder[row][col + 1] == 1:
                continue

            # 해당 위치에 사다리를 놓기
            ladder[row][col] = 1

            # 다음 위치에 사다리를 놓기 위한 재귀함수 호출
            put_ladders(count, depth + 1, row, col + 1)

            # 반환 시 다음 위치로 진행하기 위해 사다리 회수
            ladder[row][col] = 0
        # 한 행에 대한 탐색을 마치면 다음 행 1번 열부터 탐색을 시작할 수 있도록
        y = 1


def solution():
    for i in range(4):
        put_ladders(i, 0, 1, 1)
        if flag:
            return i
        
    # 3개를 초과하거나 불가능한 경우
    return -1


if __name__ == "__main__":
    print(solution())
