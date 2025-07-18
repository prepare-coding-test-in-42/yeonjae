def multiply(a, b):
    

def matrix_power(mat, n):
    if n == 1:
        return mat
    
    half = matrix_power(mat, n // 2)
    result = multiply(half, half)

