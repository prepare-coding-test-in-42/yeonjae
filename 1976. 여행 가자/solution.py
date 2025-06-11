from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        curr = queue.popleft()

        # 0-based
        for next in graph[curr - 1]:
            if next not in visited:
                visited.add(next)
                queue.append(next)
    
    return visited


def main():
    N = int(input())
    M = int(input())

    # 0-based
    graph = {i: [] for i in range(N)}
    for i in range(N):
        row = list(map(int, input().split()))
        graph[i] = list()
        for j in range(N):
            if row[j] == 1:
                graph[i].append(j + 1)
    
    plan = list(map(int, input().split()))

    visited = bfs(graph, plan[0])

    if all(city in visited for city in plan):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
