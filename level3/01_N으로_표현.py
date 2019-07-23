def has_dup(num, l, tmp):
    if num <= 0:
        return True

    if num in tmp:
        return True
    for x in l:
        if num in x:
            return True
    return False

def solution(N, number):
    if N == number:
        return 1

    answer = 0
    l = []
    while answer < 8:
        if answer == 0:
            l.append([N])
            answer += 1
            continue
        tmp = []
        for i in range((answer + 1) // 2):
            for x in l[answer - i - 1]:
                for y in l[i]:
                    if y == N and x == l[answer - 1][0]:
                        tmp.append(x * 10 + y)
                    t1 = x + y
                    t2 = x - y
                    t3 = x * y
                    t4 = x // y
                    if not has_dup(t1, l, tmp):                
                        tmp.append(t1)
                    if not has_dup(t2, l, tmp):
                        tmp.append(t2)
                    if not has_dup(t3, l, tmp):
                        tmp.append(t3)
                    if not has_dup(t4, l, tmp):
                        tmp.append(t4)
        if number in tmp:
            break
        l.append(tmp)
        answer += 1
    else:
        return -1
    return answer + 1

print(solution(5, 12))
print(solution(2, 11))
