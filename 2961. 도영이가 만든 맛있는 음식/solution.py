from itertools import combinations

def solution():
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float('inf')

    for num in range(1, N + 1):
        combs = combinations(ingredients, num)
        
        for comb in combs:
            sourness, bitterness = 1, 0
            for s, b in comb:
                sourness *= s
                bitterness += b
            min_diff = min(min_diff, abs(sourness - bitterness))
    
    return min_diff


if __name__ == "__main__":
    print(solution())