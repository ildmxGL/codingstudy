def solution(heights):
    answer = []
    for i, h in enumerate(heights):
        for j, x in enumerate(reversed(heights[:i])):
            if x > h:
                answer.append(len(heights[:i]) - j)
                break
        
        if len(answer) < i + 1:
            answer.append(0)

    return answer

