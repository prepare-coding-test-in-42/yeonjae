import sys
import math

input = sys.stdin.readline

N = int(input())
nums_of_students = list(map(int, input().split()))
B, C = map(int, input().rsplit())

def solution():
    count = 0
    for num in nums_of_students:
        count = count + 1
        if num <= B:
            continue
        num = num - B
        count = count + math.ceil(num / C)
    return count


if __name__ == "__main__":
    print(solution())