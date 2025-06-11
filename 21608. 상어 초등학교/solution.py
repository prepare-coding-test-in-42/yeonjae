def in_bounds(x, y, N):
    return 0 <= x < N and 0 <= y < N


def main():
    N = int(input())
    preference = dict()

    for _ in range(pow(N, 2)):
        row = list(map(int, input().split()))
        preference[row[0]] = row[1:]
    
    # 교실 상태 (0은 빈 자리)
    board = [[0] * N for _ in range(N)]

    # 방향 벡터 (상하좌우)
    DIRECTIONS = [(-1 , 0), (0, -1), (1, 0), (0, 1)]

    for student in preference:
        best = (-1, -1, -1, -1)
        best_pos = None

        for r in range(N):
            for c in range(N):
                if board[r][c] != 0:
                    continue

                like_cnt, empty_cnt = 0, 0
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if not in_bounds(nr, nc, N):
                        continue
                    if board[nr][nc] == 0:
                        empty_cnt += 1
                    elif board[nr][nc] in preference[student]:
                        like_cnt += 1

                if (like_cnt, empty_cnt, -r, -c) > best:
                    best = (like_cnt, empty_cnt, -r, -c)
                    best_pos = (r, c)
        
        r, c = best_pos
        board[r][c] = student

    total_score = 0
    for r in range(N):
        for c in range(N):
            student = board[r][c]
            count = 0
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if not in_bounds(nr, nc, N):
                    continue
                if board[nr][nc] in preference[student]:
                    count += 1
            # total_score += pow(10, count - 1)
            total_score += [0, 1, 10, 100, 1000][count]
    
    print(total_score)


if __name__ == "__main__":
    main()