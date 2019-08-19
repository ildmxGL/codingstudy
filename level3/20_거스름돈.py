def solution(n, money):
    cache = []
    DIV = 1000000007

    for i, v in enumerate(money):
        if i == 0:
            cache = [1 if m % money[0] == 0 else 0 for m in range(n + 1)]
            continue
        for j in range(n + 1):
            if j < v:
                continue
            else:
                cache[j] += cache[j - v]
    return cache[n] % DIV

print(solution(5, [1, 2, 5])) # 4
print(solution(10, [1, 2, 5])) # 10
print(solution(12, [2, 3, 5, 6])) # 8
