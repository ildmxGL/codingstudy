def minus124(num, idx):
    shorter = False
    if num[idx] == '1':
        if idx == 0:
            num.pop(0)
            shorter = True
        else:
            num[idx] = '4'
            shorter = minus124(num, idx - 1)
    elif num[idx] == '2':
        num[idx] = '1'
    else: # 4
        num[idx] = '2'
        shorter = minus124(num, idx - 1)
    return shorter

def solution(n):
    answer = []
    while n > 0:
        d, m = divmod(n, 3)
        answer.append(str(m) if m else '4')
        n = d
    answer.reverse()
    #print(''.join(answer))

    is_shorter = False
    tmp = [x for x in answer]
    for i in range(len(answer) - 1, 0, -1):
        if is_shorter:
            break
        if tmp[i] == '4' and answer[i] == '4':
            is_shorter = minus124(answer, i - 1)
    return ''.join(answer)

for i in range(100):
    print('{}: {}'.format(i, solution(i)))
