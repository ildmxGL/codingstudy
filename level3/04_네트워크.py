def solution(n, computers):
    lst = []
    for row in range(n):
        S = set([col for col in range(n) if computers[row][col]])
        for i in range(len(lst)):
            if lst[i] & S:
                lst[i] |= S
                break
        else:
            lst.append(S)
    return len(lst)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))       # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))       # 1
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))       # 3
print(solution(5, [[1, 1, 0, 0, 1],
                   [1, 1, 0, 1, 0],
                   [0, 0, 1, 1, 0],
                   [0, 1, 1, 1, 0],
                   [1, 0, 0, 0, 1]]))                       # 1
print(solution(5, [[1, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0],
                   [1, 0, 1, 0, 1],
                   [0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 1]]))                       # 2
print(solution(5, [[1, 1, 1, 1, 0],
                   [1, 1, 0, 1, 0],
                   [1, 0, 1, 1, 0],
                   [1, 1, 1, 1, 0],
                   [0, 0, 0, 0, 1]]))                       # 2
print(solution(5, [[1, 0, 0, 0, 0],
                   [0, 1, 1, 0, 0],
                   [0, 1, 1, 0, 1],
                   [0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 1]]))                       # 3
