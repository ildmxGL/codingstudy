def solution(n):
    answer = 0
    while n:
        d, r = divmod(n, 2)
        if r:
            answer += 1
        n = d
    return answer

print(solution(5))
print(solution(6))
print(solution(5000))
