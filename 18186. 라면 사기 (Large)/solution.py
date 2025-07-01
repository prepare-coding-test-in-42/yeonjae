N, B, C = map(int, input().split())
A = list(map(int, input().split()))

cost = 0

if C < B:
    for i in range(N):
        if i + 2 < N and A[i + 1] > A[i + 2]:
            two = min(A[i], A[i + 1] - A[i + 2])
            A[i] -= two
            A[i + 1] -= two
            cost += two * (B + C)

        if i + 2 < N:
            three = min(A[i], A[i + 1], A[i + 2])
            A[i] -= three
            A[i + 1] -= three
            A[i + 2] -= three
            cost += three * (B + C * 2)
        
        if i + 1 < N:
            two = min(A[i], A[i + 1])
            A[i] -= two
            A[i + 1] -= two
            cost += two * (B + C)
        
        cost += A[i] * B
else:
    for a in A:
        cost += a * B

print(cost)