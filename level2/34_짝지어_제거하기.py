# import string
from collections import deque

def solution(s):
    """
    # 앞에서부터 중복되면 그거 제거
    # 시간 초과
    while s:
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                s = s[:i - 1] + s[i + 1:]
                break
        else:
            return 0
    return 1
    """
    """
    # 알파벳으로 접근
    # 시간 초과

    alpha_pair = [apb * 2 for apb in string.ascii_lowercase]
    while s:
        for x in alpha_pair:
            i = s.find(x)
            if i != -1:
                s = s[:i] + s[i + 2:]
                break
        else:
            return 0
    return 1
    """
    # deque로 접근하니 해결
    # 인 줄 알았으나 s를 여러번 훑는게 아니라 끝만 보고 중복된 문자열이 answer에 안 들어가게끔 접근하면 해결됨
    s = deque(s)
    tmp = deque()
    c = len(s)
    while True:
        if not s and not tmp:
            break
        if not s:
            if c == len(tmp):
                return 0
            s, tmp = tmp, s
            c = len(s)

        e = s.popleft()
        if not tmp:
            tmp.append(e)
        elif tmp[-1] == e:
            tmp.pop()
        else:
            tmp.append(e)
    return 1

print(solution('baabaa'))
print(solution('cdcd'))
