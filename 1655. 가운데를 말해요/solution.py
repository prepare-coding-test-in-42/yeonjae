import sys
import heapq

def main():
    input = sys.stdin.readline
    N = int(input())

    left = []   # 최대 힙 (중간 이하)
    right = []  # 최소 힙 (중간 초과)

    for _ in range(N):
        num = int(input())

        heapq.heappush(left, -num)

        # 왼쪽 최대 > 오른쪽 최소이면 swap
        if right and -left[0] > right[0]:
            heapq.heappush(right, -heapq.heappop(left))
            heapq.heappush(left, -heapq.heappop(right))

        # 크기 조절
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))

        # 중간값은 항상 left 루트
        print(-left[0])


if __name__ == "__main__":
    main()
