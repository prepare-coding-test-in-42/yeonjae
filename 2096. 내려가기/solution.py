N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

prev_max = board[0][:]
prev_min = board[0][:]

for i in range(1, N):
    a0, a1, a2 = prev_max
    b0, b1, b2 = prev_min

    prev_max[0] = max(a0, a1) + board[i][0]
    prev_max[1] = max(a0, a1, a2) + board[i][1]
    prev_max[2] = max(a1, a2) + board[i][2]

    prev_min[0] = min(b0, b1) + board[i][0]
    prev_min[1] = min(b0, b1, b2) + board[i][1]
    prev_min[2] = min(b1, b2) + board[i][2]

print(max(prev_max), min(prev_min))
