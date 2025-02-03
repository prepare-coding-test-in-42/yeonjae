from collections import defaultdict, deque

def build_graph(wires):
    graph = defaultdict(list)

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return graph


def count_nodes(graph, start, cut_node):
    visited = set()
    visited.add(start)

    queue = deque([start])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1

        for neighbor in graph[node]:
            if neighbor not in visited and neighbor != cut_node:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return count


def solution(n, wires):
    min_diff = n

    graph = build_graph(wires)
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        count1 = count_nodes(graph, v1, v2)
        count2 = n - count1

        min_diff = min(min_diff, abs(count1 - count2))
        
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return min_diff