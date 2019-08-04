def solution(arrangement):
    answer = 0
    stack = []
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append(i)
        else:
            answer += len(stack) if stack.pop()+1 == i else 1
    return answer
