def solution(triangle):
    for h in range(len(triangle) - 2, -1 , -1):
        for i in range(len(triangle[h])):
            triangle[h][i] += max(triangle[h + 1][i], triangle[h + 1][i + 1])
    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
