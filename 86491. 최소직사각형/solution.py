def solution(sizes):
    width = 0
    height = 0
    # areas = set()

    # Iterate through all sizes to get all possible areas
    # for i in range(len(sizes)):
    #     width = sizes[i]
    #     for j in range(len(sizes)):
    #         height = sizes[i][j]
    #         area = width * height
    #         areas.add(area)

    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
        if (size[0] > width):
            width = size[0]
        if (size[1] > height):
            height = size[1]

    return width * height
