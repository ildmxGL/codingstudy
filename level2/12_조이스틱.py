def find_mn(idx, name):
    base = ['A'] * len(name)
    name[idx] = 'A'
    if name == base:
        return 0
    right, left = 0, 0
    ridx, lidx = idx, idx
    nw_right = [x for x in name]
    nw_left = [x for x in name]
    for _ in range(len(name)):
        if nw_right[ridx] != 'A':
            break
        ridx = (ridx + 1) % len(name)
        right += 1
    right += find_mn(ridx, nw_right)
    for _ in range(len(name)):
        if nw_left[lidx] != 'A':
            break
        lidx = lidx - 1 if lidx - 1 < 0 else len(name) - 1
        left += 1
    left += find_mn(lidx, nw_left)

    return left if left < right else right

def solution(name):
    answer = 0
    tmp = 0
    print(name)
    for x in name:
        tmp += ord(x) - ord('A') if ord(x) < ord('M') else ord('Z') + 1 - ord(x)
    name = list(name)
    idx = 0
    answer += find_mn(idx, name)
    """
    while True:
        ridx, lidx = 1, 1
        tmp += ord(name[idx]) - ord('A') if ord(name[idx]) < ord('M') else ord('Z') + 1 - ord(name[idx])
        name[idx] = 'A'
        if name == base:
            break
        for i in range(1, len(name)):
            if name[idx + i] == 'A':
                ridx += 1
            else:
                break
            if name[idx - i] == 'A':
                lidx += 1
            else:
                break
        if ridx > lidx:
            answer += lidx
            idx -= lidx
        else:
            answer += ridx
            idx += ridx
    """
    print(answer)
    return answer + tmp

print(solution('JAZ'))
print(solution('JEROEN'))
print(solution('JAAN'))
print(solution('JJAAAAAZZ'))
print(solution('JAJJJJJAAAAZZ'))
print(solution('AJJJJAAZ'))
print(solution('AAAAAAAAJJZ'))
print(solution('JJJAAAAZZ'))
print(solution('ABABAAAAABA'))
print(solution('AZAAAZ'))
print(solution('AZAAA'))
print(solution('AAAAAA'))
print(solution('BA'))
print(solution('ABA'))
print(solution('AB'))
print(solution('BAB'))
print(solution('ABAB'))
print(solution('BABA'))
print(solution('ABABA'))
print(solution('BABAB'))
print(solution('AAABAAAA'))
print(solution('AAABAAAAB'))
