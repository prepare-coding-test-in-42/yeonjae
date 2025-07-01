from heapq import heappush, heappop

N = int(input())
problems = []

for _ in range(N):
    d, r = map(int, input().split())
    problems.append((d, r))

problems.sort()

heap = []
for d, r in problems:
    heappush(heap, r)
    # 지금까지 선택한 문제들의 데드라인을 전부 만족하려면 문제 수 ≤ 해당 문제의 데드라인
    if len(heap) > d:
        # 선택한 문제 수가 현재 문제의 데드라인보다 많으면 (즉, 시간 초과 상태) 가장 가치(컵라면 수)가 낮은 문제를 pop
        heappop(heap)

print(sum(heap))
