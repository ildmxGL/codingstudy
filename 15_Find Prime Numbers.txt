# 다른 사람 코드
# 재귀함수로 했더니 최대 재귀 횟수 초과로 Runtime Error 발생
def solution(n):
    num=set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    answer = len(num)
    return answer