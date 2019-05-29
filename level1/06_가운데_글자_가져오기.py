def solution(s):
    answer = ''
    l = len(s) // 2
    r = len(s) % 2

    if r == 0:
        answer += s[l - 1 : l + 1]
    else:
        answer += s[l]

    return answer
