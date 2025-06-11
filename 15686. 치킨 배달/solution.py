from itertools import combinations

def solution():
    N, M = map(int, input().split())

    homes = []
    shops = []
    for r in range(N):
        row = input().split()
        for c in range(N):
            # Store each coordinate as a tuple (r, c)
            if row[c] == '1':
                homes.append((r, c))
            elif row[c] == '2':
                shops.append((r, c))

    min_total_dist = float("inf")
    for comb in combinations(shops, M):
        total_dist = 0
        for home in homes:
            min_shop_dist = float("inf")
            for shop in comb:
                shop_dist = abs(home[0] - shop[0]) + abs(home[1] - shop[1])
                min_shop_dist = min(min_shop_dist, shop_dist)
            total_dist += min_shop_dist
        min_total_dist = min(min_total_dist, total_dist)
    
    return min_total_dist


if __name__ == "__main__":
    print(solution())
