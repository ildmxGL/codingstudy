def solution(n):
    if n < 2:
        return n

    n_1, n_2 = 1, 0
    n_0 = 0
    for i in range(2, n + 1):
        n_0 = (n_1 + n_2) % 1234567
        n_1, n_2 = n_0, n_1
    return n_0

print(solution(3))
print(solution(5))
print(solution(100000))
