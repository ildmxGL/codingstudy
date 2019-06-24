def solution(n, a, b):
    answer = 0
    while n:
        n //= 2
        if a <= n and b <= n:
            pass
        elif a > n and b > n:
                a -= n
                b -= n
                pass
        else:
            answer += 1
            a, b = 1, n
    return answer
