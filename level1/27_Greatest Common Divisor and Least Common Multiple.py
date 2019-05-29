#gcd: greatest common divisor
#lcm: least common multiple
#s: smaller number, l: larger number
#s mod l = 0 이면 gcd(s,l) = l
#s mod l > 0 이면 gcd(s,l) = gcd(l, s mod l)
#lcm = s*l//gcd


def solution(n, m):
    answer = []
    if n < m:
        s = n
        l = m
    else:
        s = m
        l = n
    
    mod = s%l
    while mod > 0:
        s = l
        l = mod
        mod = s%l
    gcd = l
    lcm = n*m//gcd
    answer.append(gcd)
    answer.append(lcm)
    
    return answer