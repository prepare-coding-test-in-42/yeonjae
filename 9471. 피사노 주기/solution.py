P = int(input())

for _ in range(P):
    N, M = map(int, input().split())

    a, b = 0, 1

    # Pisano 주기의 최대는 M * M을 넘지 않음
    for i in range(1, M * M):
        a, b = b, (a + b) % M

        if a == 0 and b == 1:
            k = i
            break
    
    print(N, k)