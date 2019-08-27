def solution(money):
    x_0, x_1, x_2 = 0, 0, 0
    for i in range(len(money) - 1, 0, -1):
        x_1, x_2 = x_0, x_1
        if i == len(money) - 1:
            x_0 = money[i]
        elif i == len(money) - 2:
            x_0 = max(money[i], x_1)
        else:
            x_0 = max(money[i] + x_2, x_1)
    answer = max(x_0, x_1)
    x_0, x_1, x_2 = 0, 0, 0
    for i in range(len(money) - 2, -1, -1):
        x_1, x_2 = x_0, x_1
        if i == len(money) - 2:
            x_0 = money[i]
        elif i == len(money) - 3:
            x_0 = max(money[i], x_1)
        else:
            x_0 = max(money[i] + x_2, x_1)
    answer = max(answer, x_0)
    return answer

print(solution([1, 2, 3, 1])) #4
