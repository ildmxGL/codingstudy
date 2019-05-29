def solution(a, b):
    monthArray = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayArray = ['FRI', 'SAT','SUN', 'MON', 'TUE', 'WED', 'THU']
    nday = 0
    for i in range(a-1):
        nday += monthArray[i]
    nday = nday + b - 1
    dayIndex = nday%7
    answer = dayArray[dayIndex]
    return answer