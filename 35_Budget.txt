def solution(d, budget):
    answer = 0
    d.sort()
    while budget >= 0:
        if answer == len(d):
            return answer
        budget -= d[answer]
        answer += 1
    answer -= 1
    return answer