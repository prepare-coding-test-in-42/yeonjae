from collections import deque

DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def main():
    N, M, fuel = map(int, input().split())
    board = []
    walls = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 1:
                walls.append((r, c))
        board.append(row)
    
    start_x, start_y = map(int, input().split())

    guests = []
    for r in range(M):
        row = list(map(int, input().split()))
        guests.append(row)
    
    visited = set([(start_x, start_y)])
    queue = deque([])


if __name__ == "__main__":
    main()