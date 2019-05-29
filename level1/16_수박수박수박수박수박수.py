def solution(n):
    answer = ''
    while n > 0:
        if answer == '':
            answer += '수'
            n -= 1
            continue
        answer += '박' if answer[-1] == '수' else '수'
        n -= 1

    return answer
