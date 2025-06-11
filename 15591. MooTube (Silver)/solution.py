from collections import defaultdict, deque

def bfs(graph, start, k):
    queue = deque([start])
    count = 0
    visited = set([start])

    while queue:
        curr = queue.popleft()

        for next, weight in graph[curr]:
            if next not in visited and weight >= k:
                visited.add(next)
                queue.append(next)
                count += 1
    
    return count


def main():
    N, Q = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(N - 1):
        p, q, r = map(int, input().split())
        graph[p].append((q, r))
        graph[q].append((p, r))

    questions = []
    for _ in range(Q):
        questions.append(list(map(int, input().split())))

    for k, v in questions:
        answer = bfs(graph, v, k)
        print(answer)


if __name__ == "__main__":
    main()