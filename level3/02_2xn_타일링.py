"""
# 시간 초과
def solution(n):
    if n < 3:
        return n
    
    lst = []
    lst.append(set('1'))            # n = 1
    lst.append(set(['11', '00']))   # n = 2
    for m in range(3, n + 1):
        S = set()
        for i in range(m // 2):
            print('lst: {}'.format(lst))
            print('i: {}'.format(i))
            for x in lst[i]:
                for y in lst[m - i - 2]:
                    S.add(x + y)
                    S.add(y + x)
        lst.append(S)
    print(lst)
    return len(lst[n - 1]) % 1000000007
"""
def solution(n):
    if n < 3:
        return n
    i_2 = 1
    i_1 = 2
    n -= 2
    while n:
        i_1, i_2 = (i_1 + i_2) % 1000000007, i_1
        n -=1
    return i_1

print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
