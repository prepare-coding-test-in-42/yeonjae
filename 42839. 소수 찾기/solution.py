import math
from itertools import permutations

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    # digits = []
    # for number in numbers:
    #     digits.append(int(number))
    digits = list(numbers)  # "123" -> ['1', '2', '3']
    
    # combs = []
    # for i in range(len(digits)):
    #     combs.extend(combinations(digits, i + 1))

    # perms = set()
    # for comb in combs:
    #     perms.update(permutations(comb))

    results = set()
    # for perm in perms:
    #     result = 0
    #     for idx in range(len(perm)):
    #         results.add(perm[idx])
    #         result += perm[idx] * 10 ** idx
    #     results.add(result)

    # 가능한 모든 자릿수의 순열을 생성하여 숫자로 변환 후 추가
    for i in range(1, len(digits) + 1):
        for perm in permutations(digits, i):
            # 순열을 문자열로 합친 후 정수로 변환
            number = int(''.join(perm))
            # results set에 추가해 중복 제거
            results.add(number)

    for result in results:
        if is_prime(result):
            answer += 1

    return answer
