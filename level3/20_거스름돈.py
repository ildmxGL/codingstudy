DIV = 1000000007
S = 0

def pay_func(pay, money, idx = 0, s = 0):
    global S
    if idx >= len(money): return 0

    c = 0
    while True:
        tmp = money[idx] * c
        if tmp > pay: return 0
        elif tmp == pay: 
            S += 1
            break

        pay_func(pay - tmp, money, idx + 1, s)
        c += 1
    return S % DIV

def solution(n, money):
    money.sort()
    return pay_func(n, money)

print(solution(5, [1, 2, 5]))
