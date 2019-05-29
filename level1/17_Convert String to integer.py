def solution(s):
    #answer = int(s) #문제에서 원하는 정답이 아닌 것 같다.
    answer = 0
    positive = True
    num = 0
    
    if s[0] == '+':
        s.replace('+','')
        
    elif s[0] == '-':
        positive = False
        s.replace('-','')
    
    for i in range(len(s)):
        if s[i] == '0':
            num = 0
        elif s[i] == '1':
            num =1
        elif s[i] == '2':
            num =2
        elif s[i] == '3':
            num =3
        elif s[i] == '4':
            num =4
        elif s[i] == '5':
            num =5
        elif s[i] == '6':
            num =6
        elif s[i] == '7':
            num =7
        elif s[i] == '8':
            num =8
        elif s[i] == '9':
            num =9
        answer += num * 10**(len(s)-i-1)
    if positive == False:
        answer *= -1
            
    return answer