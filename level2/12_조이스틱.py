def solution(name):
    answer = 0
    tmp = 0
    print(name)
    idxes = []
    current_idx = 0
    n = len(name)
    for i, x in enumerate(name):
        tmp += ord(x) - ord('A') if ord(x) < ord('M') else ord('Z') + 1 - ord(x)
        if x != 'A':
            idxes.append(i)
    while idxes:
        min_dist = float('inf')
        min_idx = 0
        for it in idxes:
            min_dist2 = min(abs(it - current_idx), n - abs(it - current_idx))
            if min_dist2 < min_dist:
                min_dist = min_dist2
                min_idx = it
        answer += min_dist
        idxes.remove(min_idx)
        current_idx = min_idx
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
