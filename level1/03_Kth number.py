def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0] - 1
        j = c[1]
        k = c[2] - 1
        newArray = array[i:j]
        newArray.sort()
        num = newArray[k]
        answer.append(num)
    return answer