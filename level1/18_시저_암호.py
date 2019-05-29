def solution(s, n):
    answer = ''
    for x in list(s):
        if ord(x) in range(ord('a'), ord('z') + 1):
            a = ord(x) + n
            if a > ord('z'):
                a -= 26
        elif ord(x) in range(ord('A'), ord('Z') + 1):
            a = ord(x) + n
            if a > ord('Z'):
                a -= 26
        else:
            a = ord(' ')

        answer += chr(a)
    
    return answer
