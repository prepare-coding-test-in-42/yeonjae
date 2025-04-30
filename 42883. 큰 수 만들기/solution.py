def solution(number, k):
    # digits = list(number)
    # numbers = []
    
    # for comb in combinations(digits, len(number) - k):
    #     numbers.append(int(''.join(comb)))
       
    # return str(max(numbers))

    # count = 0
    # while count != k:
    #     for idx in range(len(digits) - 1):
    #         if int(digits[idx]) < int(digits[idx + 1]):
    #             digits.pop(idx)
    #             count += 1
    #             break
    #         if idx == len(digits) - 2 and count == k - 1:
    #             digits.pop(idx + 1)
    
    stack = []
    for digit in number:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # 남은 k만큼 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)