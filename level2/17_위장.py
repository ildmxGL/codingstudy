'''
import collections
from itertools import combinations
from functools import reduce

def multiply(arr):
    return reduce(lambda x,y: x*y, arr)

def solution(clothes):
    answer = 0
    kinds = collections.Counter([x[1] for x in clothes]).values()
    for i in range(len(kinds)):
        kindsCase = combinations(kinds, i+1)
        for j in kindsCase:
            answer += multiply(j)
    return answer


#테스트 1 시간 초과
'''

#combinations() 안 써도 됨

import collections

def solution(clothes):
    kinds = collections.Counter([x[1] for x in clothes]).values()
    answer = 1
    for i in kinds:
        answer *= (i+1) 
    return answer-1

'''
reduce를 이용한 다른 사람 풀이

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''