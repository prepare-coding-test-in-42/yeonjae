from collections import deque, defaultdict

def bfs(board):
    queue = deque([1])
    visited = [False] * 101
    visited[1] = True
    dist = [0] * 101

    while queue:
        curr = queue.popleft()

        for dice in range(1, 7):
            next = curr + dice
            if next > 100:
                continue

            jump = board[next]
            if not visited[jump]:
                visited[jump] = True
                dist[jump] = dist[curr] + 1
                queue.append(jump)
        
    return dist[100]


def main():
    N, M = map(int, input().split())
    board = [i for i in range(101)]

    for _ in range(N):
        k, v = map(int, input().split())
        board[k] = v
    
    for _ in range(M):
        k, v = map(int, input().split())
        board[k] = v
    
    dist = bfs(board)

    print(dist)
    

if __name__ == "__main__":
    main()