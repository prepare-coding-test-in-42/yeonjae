# from math import sqrt

# def solution(brown, yellow):
#     a = 1
#     b = -(2 + 0.5 * brown)
#     c = yellow + brown

#     width = ((-1 * b) + sqrt(abs(b ** 2 - 4 * a * c))) // 2 * a
#     height = (brown + yellow) // width
    
#     return [width, height]


def solution(brown, yellow):
    total = brown + yellow

    for width in range(1, brown):
        if total % width == 0:
            height = total // width
            if height > width:
                continue
            if (width - 2) * (height - 2) == yellow and (width + height - 2) * 2 == brown:
                return [width, height]
            
