from cmath import inf
from heapq import heappush, heappop

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_bounds(x, y, N):
    return 0 <= x < N and 0 <= y < N

def main():
    idx = 0
    while True:
        idx += 1
        N = int(input())
        if (N == 0):
            break
        
        cave = []
        for _ in range(N):
            cave.append(list(map(int, input().split())))
        
        dp = [[inf] * N for _ in range(N)]
        dp[0][0] = cave[0][0]
        heap = []
        heappush(heap, (dp[0][0], 0, 0))

        while heap:
            cost, x, y = heappop(heap)

            # 이미 더 작은 비용으로 처리된 적 있으면 continue
            if dp[x][y] < cost:
                continue

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if in_bounds(nx, ny, N):
                    new_cost = cost + cave[nx][ny]
                    if new_cost < dp[nx][ny]:
                        dp[nx][ny] = new_cost
                        heappush(heap, (new_cost, nx, ny))
        
        print(f"Problem {idx}: {dp[N - 1][N - 1]}")
        

if __name__ == "__main__":
    main()