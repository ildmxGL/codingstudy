def solution(s):
    answer = True
    if len(s) != 4 and len(s) !=6:
        return False
    
    try:
        test = int(s)
    except ValueError:
        return False
    
    return answer