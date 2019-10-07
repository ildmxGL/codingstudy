def solution(s):
    left = 0
    for i in s:
        if i == "(":
            left += 1
        else:
            if left == 0:
                return False
            left -= 1
    return True if left==0 else False


'''
다른사람풀이

def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

'''