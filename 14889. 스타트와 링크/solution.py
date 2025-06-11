from itertools import combinations


def solution():
    # 입력 받기
    N = int(input().rstrip())
    stats = [list(map(int, input().split())) for _ in range(N)]

    people = range(N)
    min_diff = float('inf')

    # N명을 N/2로 나누는 모든 경우의 수 탐색
    for start in combinations(people, N // 2):
        link = [p for p in people if p not in start]

        # 스타트 팀 능력치 계산
        start_sum = 0
        for i, j in combinations(start, 2):
            start_sum += stats[i][j] + stats[j][i]
        
        # 링크 팀 능력치 계산
        link_sum = 0
        for i, j in combinations(link, 2):
            link_sum += stats[i][j] + stats[j][i]
        
        # 최소 차이 갱신
        diff = abs(start_sum - link_sum)
        min_diff = min(min_diff, diff)

        # 차이가 0이면 최적
        if min_diff == 0:
            break

    print(min_diff)
    

if __name__ == "__main__":
    solution()