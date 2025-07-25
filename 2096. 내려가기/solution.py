N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

prev_max = board[0][:]
prev_min = board[0][:]

for i in range(1, N):
    row = board[i]

    # 현재 행에 대한 최대, 최소 점수 임시 저장
    curr_max = [0] * 3
    curr_min = [0] * 3

    for j in range(3):
        if j == 0:
            curr_max[j] = max(prev_max[j], prev_max[j + 1]) + row[j]
            curr_min[j] = min(prev_min[j], prev_min[j + 1]) + row[j]
        elif j == 1:
            curr_max[j] = max(prev_max[j - 1], prev_max[j], prev_max[j + 1]) + row[j]
            curr_min[j] = min(prev_min[j - 1], prev_min[j], prev_min[j + 1]) + row[j]
        else:
            curr_max[j] = max(prev_max[j - 1], prev_max[j]) + row[j]
            curr_min[j] = min(prev_min[j - 1], prev_min[j]) + row[j]

    prev_max = curr_max
    prev_min = curr_min

print(max(prev_max), min(prev_min))
