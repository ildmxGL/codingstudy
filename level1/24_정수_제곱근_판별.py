import math

def solution(n):
    return int(pow(math.sqrt(n) + 1, 2)) if int(math.sqrt(n)) == math.sqrt(n) else -1
