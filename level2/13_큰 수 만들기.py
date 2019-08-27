def solution(number, k):
    answer = ''
    k_count = set()
    for i in range(1,len(number)):
        for j in range(i-1,-1,-1):
            if len(k_count) == k:
                break
            if number[i] > number[j]:
                k_count.add(j)
            else:
                break
        if len(k_count) == k:
            break
    if len(k_count) < k:
        number = number[:-k+len(k_count)]
    for i in range(len(number)):
        if i in k_count:
            continue
        answer += number[i]
    
    return answer

