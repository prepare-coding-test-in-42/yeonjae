N = int(input())

start_x, start_y = map(int, input().split())
prev_x, prev_y = start_x, start_y
total_distance = 0

for i in range(N):
    # 고객의 위치 입력
    curr_x, curr_y = map(int, input().split())
    # 맨해튼 거리 계산
    if i == N - 1:
        dist = abs(prev_x - curr_x) + abs(prev_y - curr_y)
    else:
        dist = abs(prev_x - curr_x) + abs(prev_y - curr_y) - 1
    # 인접 칸까지 허용
    if dist > 1:
        dist -= 1
    total_distance += dist
    prev_x, prev_y = curr_x, curr_y

print(total_distance)