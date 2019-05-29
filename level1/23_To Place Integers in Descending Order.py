def solution(n):
    answer = 0
    st = str(n)
    sor = sorted(st) #sor is the list
    for i in range(len(sor)):
        answer += int(sor[i]) * 10**i
    return answer