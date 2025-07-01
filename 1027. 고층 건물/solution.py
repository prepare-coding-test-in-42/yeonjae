def can_see(i, j, buildings):
    # 두 빌딩 사이에 있는 다른 빌딩이 두 빌딩을 잇는 직선을 가로막지 않는지 확인
    # (0, i) ... (1, j)를 잇는 1차함수 idx에서의 함숫값
    x1, y1 = i, buildings[i]
    x2, y2 = j, buildings[j]

    for k in range(i + 1, j):
        xk, yk = k, buildings[k]
        if yk >= y1 + (y2 - y1) * (xk - x1) / (x2 - x1):
            return False
    return True
    

def check_sides(curr, buildings):
    # 현재 서 있는 빌딩의 왼편 확인
    count = 0
    for left in range(0, curr):
        if can_see(left, curr, buildings):
            count += 1
    for right in range(curr + 1, len(buildings)):
        if can_see(curr, right, buildings):
            count += 1
    return count


def main():
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0

    if N == 1:
        result = 0
    elif N == 2:
        result = 1
    else:
        for idx in range(len(buildings)):
            num_of_other_buildings = check_sides(idx, buildings)
            result = max(num_of_other_buildings, result)

    print(result)


if __name__=="__main__":
    main()