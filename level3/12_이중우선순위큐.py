def solution(operations):
    lst = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if op == 'I':
            lst.append(num)
            lst.sort()
        else:   # op == 'D'
            if not lst:
                continue

            if num == 1:
                lst.pop()
            else:   # num == -1
                lst.pop(0)
    return [max(lst), min(lst)] if lst else [0, 0]

print(solution(['I 16', 'D 1']))
print(solution(['I 7', 'I 5', 'I -5', 'D -1']))
