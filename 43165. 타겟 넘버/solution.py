def solution(numbers, target):
    # 가능한 경우의 수를 저장
    count = 0

    def dfs(index, total):
        # 중첩 함수(inner function) 안에서 바깥 함수의 변수를 수정할 때 사용되는 키워드
        nonlocal count

        # 모든 숫자를 다 사용한 경우
        if index == len(numbers):
            # 목표값과 비교
            if total == target:
                count += 1
            return
        
        # 현재 숫자를 더하는 경우
        dfs(index + 1, total + numbers[index])
        # 현재 숫자를 빼는 경우
        dfs(index + 1, total - numbers[index])
    
    # 첫 번째 숫자부터 탐색 시작
    dfs(0, 0)
    return count
