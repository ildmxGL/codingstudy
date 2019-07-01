def solution(n, a, b):
    answer = 0
    while n > 1:
        n //= 2
        if a <= n and b <= n:
            continue
        elif a > n and b > n:
                a -= n
                b -= n
                continue
        else:
            answer += 1
            a, b = 1, n
    return answer

print(solution(8, 4, 7))
