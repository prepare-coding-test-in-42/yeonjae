from collections import deque

def solution():
    gears = [deque(map(int, input().strip())) for _ in range(4)]
    K = int(input().strip())
    spins = [list(map(int, input().split())) for _ in range(K)]

    for gear_idx, direction in spins:
        gear_idx -= 1   # 0-based index

        # 회전 방향 기록: (기어 번호, 방향)
        rotate_dir = [0] * 4
        rotate_dir[gear_idx] = direction

        # 왼쪽 탐색
        for i in range(gear_idx - 1, -1, -1):
            # i번 톱니바퀴의 오른쪽 톱니와 i + 1번 톱니바퀴의 왼쪽 톱니를 비교
            if gears[i][2] != gears[i + 1][6]:
                rotate_dir[i] = -rotate_dir[i + 1]
            else:
                break
        
        # 오른쪽 탐색
        for i in range(gear_idx + 1, 4):
            # 이미 회전한 i - 1번 톱니바퀴와 지금 회전시킬지 말지 판단 중인 i번 톱니바퀴를 비교
            if gears[i - 1][2] != gears[i][6]:
                rotate_dir[i] = -rotate_dir[i - 1]
            else:
                break

        # 회전 실행
        for i in range(4):
            if rotate_dir[i] == 1:
                gears[i].rotate(1)
            elif rotate_dir[i] == -1:
                gears[i].rotate(-1)
        
    # 점수 계산
    score = 0
    for i in range(4):
        if gears[i][0] == 1:
            score += (1 << i)

    print(score)


if __name__ == "__main__":
    solution()