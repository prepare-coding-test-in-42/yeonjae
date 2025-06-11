def dfs(index):
    global max_broken

    # 종료 조건
    if index == N:
        # 모든 계란을 한 번씩 다 들었으면 현재 깨진 계란 수를 세서 최댓값 갱신
        broken = sum(1 for d in durability if d <= 0)
        max_broken = max(max_broken, broken)
        return

    # 현재 손에 든 계란이 깨졌거나, 칠 수 있는 계란이 없는 경우 다음 계란으로 넘어가기 (dfs 호출)
    if durability[index] <= 0 or all(durability[i] <= 0 or i == index for i in range(N)):
        dfs(index + 1)
        return

    for i in range(N):
        # i번째 계란이 index가 아니고, 둘 다 안 깨졌을 때만 타격 시도
        if i != index and durability[i] > 0:

            # 타격 전 상태 저장
            s1, s2 = durability[index], durability[i]

            # 내구도 갱신 (서로의 무게만큼 감소)
            durability[index] -= weight[i]
            durability[i] -= weight[index]

            # 다음 계란으로 넘어감 (dfs 호출)
            dfs(index + 1)

            # 상태 복구
            durability[index], durability[i] = s1, s2


def main():
    global N, durability, weight, max_broken

    N = int(input())
    durability = []
    weight = []
    for _ in range(N):
        d, w = map(int, input().split())
        durability.append(d)
        weight.append(w)

    max_broken = 0
    dfs(0)
    print(max_broken)


if __name__ == "__main__":
    main()