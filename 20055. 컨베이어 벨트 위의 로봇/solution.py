from collections import deque

def solution():
    N, K = map(int, input().split())
    belt = deque(map(int, input().split()))
    robot = deque([False] * N)

    step = 0
    while (True):
        step += 1

        # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
        belt.rotate(1)
        robot.rotate(1)
        robot[N - 1] = False

        # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
        for idx in range(N - 2, -1, -1):
            if robot[idx] and not robot[idx + 1] and belt[idx + 1] > 0:
                robot[idx] = False
                robot[idx + 1] = True
                belt[idx + 1] -= 1
        robot[N - 1] = False

        # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if belt[0] > 0:
            robot[0] = True
            belt[0] -= 1
        
        # 내구도 0인 칸이 K개 이상이면 종료
        if belt.count(0) >= K:
            break
    
    return step


if __name__ == "__main__":
    print(solution())