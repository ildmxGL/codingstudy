from itertools import permutations

def solution(numbers):
    item = [int(x) for x in list(numbers)]
    
    AllTuples = set()
    for length in range(1,len(item)+1):
        AllTuples.update(permutations(item, length))
        
    AllNumbers = set()
    for t in AllTuples:
        num = 0
        deg = 0
        for i in t:
            num += i*10**deg
            deg +=1
        AllNumbers.add(num)

    '''
    여기까지가 아래와 동일
        a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    '''
        
    NotPrime = set([0,1])
    for num in AllNumbers:
        for i in range(2, num):
            if num%i == 0:
                NotPrime.add(num)
                break
                
    answer = AllNumbers - NotPrime
    return len(answer)



#다른사람풀이
'''
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
'''