def solution(arr):
    answer = []
    num = arr[0]
    answer.append(num)
    for i in arr:
        if i != num:
            answer.append(i)
            num = i
    return answer