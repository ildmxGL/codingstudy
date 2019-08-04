def solution(arrangement):
    answer = 0
    stack = []
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            answer += len(stack) if arrangement[i-1] == '(' else 1
    return answer
