N = int(input())
A = list(map(int, input().split()))

cost = 0

for i in range(N):
    # print(f"i = {i}, A[i:i + 3] = {A[i:i + 3]}")

    # A = [1, 3, 2]
    # A = [0, 2, 2] -> 5원
    # A = [0, 1, 1] -> 3원
    # A = [0, 0, 0] -> 3원

    # A = [1, 3, 2]
    # A = [0, 2, 1] -> 7원
    # A = [0, 1, 0] -> 5원
    # A = [0, 0, 0] -> 3원

    if i + 2 < N and A[i + 1] > A[i + 2]:
        two = min(A[i], A[i + 1] - A[i + 2])
        A[i] -= two
        A[i + 1] -= two
        cost += two * 5

    if i + 2 < N:
        three = min(A[i], A[i + 1], A[i + 2])
        A[i] -= three
        A[i + 1] -= three
        A[i + 2] -= three
        cost += three * 7
    
    if i + 1 < N:
        two = min(A[i], A[i + 1])
        A[i] -= two
        A[i + 1] -= two
        cost += two * 5
    
    cost += A[i] * 3

print(cost)