def solution(arr):
    answer = []
    sor = sorted(arr)
    small = sor[0]
    for i in arr:
        if i != small:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer



#���� ���� �ڵ�. �� �� �ɱ�?
def solution(arr):
    answer = []
    smaller = arr[0]
    for i in arr[1:]:
        if i < smaller:
            answer.append(smaller)
            smaller = i
            continue
        answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer