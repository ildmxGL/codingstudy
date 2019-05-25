def solution(phone_number):
    answer = ''
    for i in range(-4,0):
        answer = answer + phone_number[i]
    answer = '*'*(len(phone_number)-4) + answer
    return answer