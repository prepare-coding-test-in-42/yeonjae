def solution(arr):
    stack = []
    for num in arr:
        if not stack or (stack and stack[-1] != num):
            stack.append(num)

    return stack
