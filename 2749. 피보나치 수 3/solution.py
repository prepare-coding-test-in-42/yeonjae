def multiply(a, b):
    mod = 1_000_000
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod],
    ]

def matrix_power(mat, n):
    if n == 1:
        return mat
    
    half = matrix_power(mat, n // 2)
    result = multiply(half, half)

    if n % 2 == 1:
        result = multiply(result, mat)
    
    return result

def main():
    n = int(input())

    if n == 0:
        print(0)
        return
    
    mat = [[1, 1],
           [1, 0]]
    
    print(matrix_power(mat, n)[0][1] % 1_000_000)

if __name__ == "__main__":
    main()