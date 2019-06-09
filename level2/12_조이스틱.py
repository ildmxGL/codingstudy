def count_diff_alphabet(alpha):
    return ord(alpha) - ord('A') if ord(alpha) < ord('M') else ord('Z') + 1 - ord(alpha)

def solution(name):
    print(name)
    answer = 0

    for x in name:
        answer += count_diff_alphabet(x)
    tmp = answer
    
    len_long_A = 0
    for i in range(name.count('A'), 0, -1):
        if 'A' * i in name:
            len_long_A = i
            break
    idx_long_A = name.index('A' * len_long_A)
    
    """
    # Candidates of movement
    # let name: [a, b, c]; b is length of 'AA...A'
    # consider [AA...A, a, b, c] or [a, b, c, AA...A]
    # 1) a, b, c
    # 2) a, a', c
    # 3) c, c', a
    """
    a = idx_long_A
    b = len_long_A
    c = len(name[idx_long_A + len_long_A:])

    a1 = 0
    b1 = 0
    while(name != 'A' * len_long_A and name[len(name) - 1 - a1] == 'A'):
        a1 += 1
    while(name != 'A' * len_long_A and name[len(name) - 1 - b1] == 'A'):
        b1 += 1
    if a1 == len_long_A:
        a1 = 0
    if b1 == len_long_A:
        b1 = 0

    cand_move =[]
    cand_move.append(len(name) - 1 - b1)
    cand_move.append(a * 2 - 2 + c if a else c)
    cand_move.append(c * 2 - 1 + a if c or a else 0)
    cand_move.append(c * 2 - 1 + a * 2 - 1 - a1 if c and a else min(cand_move))
    cand_move.append(a * 2 - 2 + c * 2 - 1 - b1 if a and c else cand_move[-1])
    print(cand_move)

    answer += min(cand_move)
    
    print(answer - tmp)
    return answer

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
