def solution(progresses, speeds):
    CMPLT = 100

    baepoe_dates = []
    for i in range(0, len(progresses)):
        d, m = divmod(CMPLT - progresses[i], speeds[i])
        baepoe_dates.append(d if m == 0 else d + 1)

    max_date = baepoe_dates[0]
    answer = [1]
    for i in range(1, len(baepoe_dates)):
        if baepoe_dates[i] > max_date:
            answer.append(1)
            max_date = baepoe_dates[i]
        else:
            answer[-1] += 1

    return answer

print(solution([93, 30, 55], [1, 30, 5]))

