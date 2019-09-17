def solution(brown, red):
    S = brown + red
    cases_red = []
    i = 1
    while red//i >= i:
        if red%i == 0:
            cases_red.append((red//i, i))
        i += 1
    a=1
    while True:
        for x in cases_red:
            if (x[0] + 2*a)*(x[1] + 2*a) == S:
                return [(x[0] + 2*a), (x[1] + 2*a)]
        a += 1
        
        
'''
다른 사람 풀이

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
'''