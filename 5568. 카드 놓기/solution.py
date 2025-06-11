from itertools import permutations

def solution():
    n = int(input())
    k = int(input())

    cards = []
    for _ in range(n):
        cards.append(input())
    
    perms = permutations(cards, k)
    result = set()

    for perm in perms:
        number = ''.join(perm)
        result.add(int(number))
    
    return len(result)


if __name__=="__main__":
    print(solution())