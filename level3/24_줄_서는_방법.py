"""
# 시간 초과
from itertools import permutations

def solution(n, k):
    return list(map(int, list(permutations(map(str, range(1, n + 1))))[k - 1]))
"""

from math import factorial

def func(n, k, idx, answer):
    if idx == n:
        return
        #return False if k else True

    for i in range(1, n + 1):
        if i in answer: continue
        
        tmp = factorial(n - idx - 1)
        if tmp < k:
            k -= tmp
            continue
        elif tmp > k:
            answer.append(i)
            func(n, k, idx + 1, answer)
        else:
            answer.append(i)
            for j in range(n, 0, -1):
                if j in answer: continue
                answer.append(j)
            break
    return

def solution(n, k):
    answer = []
    idx = 0
    func(n, k, 0, answer)
    
    return answer

print(solution(3, 5)) # [3, 1, 2]
print(solution(4, 20)) # [4, 1, 3, 2]
