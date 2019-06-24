def isSquare(board, point, length):
    if point[0] + length > len(board) or point[1] + length > len(board[0]):
        return False

    for x in board[point[0]:point[0] + length]:
        if 0 in x[point[1]:point[1] + length]:
            return False
    return True

def solution(board):
    for x in board:
        print(x)
    point = [0, 0]
    answer = 0
    while True:
        cndt_ans = answer + 1
        while isSquare(board, point, cndt_ans):
            cndt_ans += 1
        else:
            cndt_ans -= 1
        answer = cndt_ans if cndt_ans > answer else answer

        point[1] = (point[1] + 1) % len(board[0])
        point[0] = point[0] + 1 if point[1] == 0 else point[0]
        if point[0] == len(board):
            break
    return pow(answer, 2)

print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0]]))
