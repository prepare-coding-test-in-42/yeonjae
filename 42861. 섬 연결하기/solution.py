def solution(n, costs):
    answer = 0

    # 비용 순 정렬
    costs.sort(key=lambda x : x[2])

    # 시작점 포함
    linked = {costs[0][0]}
    
    while len(linked) != n:
        for start, end, cost in costs:
            # 이미 연결된 다리는 건너뜀
            if start in linked and end in linked:
                continue
            # 적어도 하나만 연결된 경우 확장
            if start in linked or end in linked:
                linked.update([start, end])
                answer += cost
                break

    return answer
