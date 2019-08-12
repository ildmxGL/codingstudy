DIV = 1000000007
S = 0
"""
# 시간 초과 4/6 실패
def pay_func(n, money):
    global S
    if len(money) == 1:
        if n % money[0] == 0:
            S += 1
        return

    for i in range(len(money) - 1, -1, -1):
        if money[i] > n:
            continue
        if money[i] == n:
            S = (S + 1) % DIV
            continue

        pay_func(n - money[i], money[:i + 1])
    return
"""

def pay_func(n, money):
    global S
    if not money:
        return
    if len(money) == 1:
        if n % money[0] == 0:
            S = (S + 1) % DIV
        return

    for i in range(len(money) - 1, -1, -1):
        for t in range(n // money[i], 0, -1):
            x = money[i] * t
            if x == n:
                S = (S + 1) % DIV
                continue

            pay_func(n - x, money[:i])

    return

def solution(n, money):
    pay_func(n, sorted(money))
    return S

print(solution(5, [1, 2, 5])) # 4
