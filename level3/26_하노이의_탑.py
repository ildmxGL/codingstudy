def solution(n):
    poles = [1, 2, 3]
    def hanoi(n, start, goal, answer):
        if n == 1:
            answer.append([start, goal])
            return

        rest_pole = 0
        for p in poles:
            if p != start and p != goal:
                rest_pole = p

        hanoi(n - 1, start, rest_pole, answer)
        answer.append([start, goal])
        hanoi(n - 1, rest_pole, goal, answer)

        return 

    answer = []
    hanoi(n, 1, 3, answer)
    return answer

print(solution(2)) # [[1, 2], [1, 3], [2, 3]]
