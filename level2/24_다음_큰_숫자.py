def solution(n):
    count_n = format(n, 'b').count('1')
    answer = n + 1
    while True:
        if format(answer, 'b').count('1') == count_n:
            break
        answer += 1
    return answer

print(solution(78))
print(solution(15))
