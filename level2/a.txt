def solution(baseball):
    answer = 0
    for num in range(100, 1000):
        num = str(num)
        if num[1] == '0' or num[2] == '0':
            continue
        if num[0] == num[1] or num[1] == num[2] or num[2] == num[0]:
            continue
        
        for x in baseball:
            x0 = str(x[0])
            strike = 0
            ball = 0

            for i in range(len(x0)):
                if num[i] == x0[i]:
                    strike += 1
                if num[i] in x0 and num[i] != x0[i]:
                    ball += 1

            if (strike, ball) != (x[1], x[2]):
                break
        else:
            answer += 1

    return answer

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
