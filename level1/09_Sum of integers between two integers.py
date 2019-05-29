def solution(a, b):
    answer = 0
    if a < b:
        s = a
        l = b
    else:
        s = b
        l = a
    for i in range(s,l+1):
        answer += i
    return answer