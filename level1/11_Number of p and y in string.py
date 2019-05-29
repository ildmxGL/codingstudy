def solution(s):
    answer = True
    pConter = 0
    yConter = 0
    for i in s:
        if i == 'P' or i == 'p':
            pConter += 1
        elif i == 'Y' or i == 'y':
            yConter += 1
    if pConter != yConter:
        answer = False
    
    return answer