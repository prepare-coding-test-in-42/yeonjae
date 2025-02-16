def solution(n, computers):
    # 연결된 네트워크 개수
    count = 0
    # 방문 여부 체크
    visited = [False] * n

    def dfs(node):
        # 현재 노드 방문 처리
        visited[node] = True
        # 모든 컴퓨터를 확인
        for i in range(n):
            # 연결된 컴퓨터가 있고 방문하지 않았다면
            if computers[node][i] == 1 and not visited[i]:
                # 재귀 호출을 통해 연결된 컴퓨터로 이동
                dfs(i)
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    
    return count