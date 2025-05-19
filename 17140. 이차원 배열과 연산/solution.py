from collections import Counter


def r_operation(A):
    new_A = []
    max_len = 0

    for row in A:
        counter = Counter([num for num in row if num != 0])
        sorted_items = sorted(counter.items(), key=lambda x : (x[1], x[0]))
        new_row = []
        for num, cnt in sorted_items:
            new_row += [num, cnt]
        max_len = max(max_len, len(new_row))
        new_A.append(new_row)
    
    for i in range(len(new_A)):
        new_A[i] += [0] * (max_len - len(new_A[i]))
        new_A[i] = new_A[i][:100]
    
    return new_A


def c_operation(A):
    cols = list(zip(*A))
    max_len = 0
    new_cols = []
    for col in cols:
        counter = Counter([num for num in col if num != 0])
        sorted_items = sorted(counter.items(), key=lambda x : (x[1], x[0]))
        new_col = []
        for num, cnt in sorted_items:
            new_col += [num, cnt]
        new_cols.append(new_col)
    
    max_len = max(len(col) for col in new_cols)
    for i in range(len(new_cols)):
        new_cols[i] += [0] * (max_len - len(new_cols[i]))
        new_cols[i] = new_cols[i][:100]
    
    return list(map(list, zip(*new_cols)))


def main():
    r, c, k = map(int, input().split())
    A = []
    for _ in range(3):
        A.append(list(map(int, input().split())))

    for sec in range(101):
        if 0 <= r - 1 < len(A) and 0 <= c - 1 < len(A[0]):
            if A[r - 1][c - 1] == k:
                print(sec)
                return
        
        if len(A) < len(A[0]):
            A = c_operation(A)
        else:
            A = r_operation(A)
    
    print(-1)

if __name__ == "__main__":
    main()