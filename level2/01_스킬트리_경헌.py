"""
# yeji's solution
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        n = -1 #index
        e = False #error
        for i in skill:
            m = tree.find(i)
            if n <= m:
                n = m
            else:
                e = True
                break
        if e == False:
            answer += 1
    return answer
"""

def idx_skill(skill, skill_tree):
    try:
        idx = skill_tree.index(skill)
    except ValueError:
        idx = float('inf')
    return idx

def solution(skill, skill_trees):
    answer = 0
    for x in skill_trees:
        idx_list = [idx_skill(y, x) for y in skill]
        # runtime error
        #answer += min([0 if idx_list[i] < max(idx_list[:i]) else 1 for i in range(1, len(idx_list))])
        tmp = 1
        for i in range(1, len(idx_list)):
            # 왜 부등호 바꿔서 if랑 else block을 뒤집으면 테스트 통과가 안 될까?
            if idx_list[i] < max(idx_list[:i]):
                tmp = 0
                break
            else:
                continue
        answer += tmp
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
