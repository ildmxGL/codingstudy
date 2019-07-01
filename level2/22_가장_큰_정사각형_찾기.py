def solution(board):
    ss = {}
    answer = 0
    for y, line in enumerate(board):
        for x, v in enumerate(line):
            if v == 0:
                continue
            ss[(x, y)] = s = min(ss.get((x-1, y), 0),
                                 ss.get((x-1, y-1), 0),
                                 ss.get((x, y-1), 0)
                                 ) + 1
            answer = max(answer, s)
    return answer ** 2

print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
print(solution([[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]]))
