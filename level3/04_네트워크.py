# 서로 이어지지 않았지만 한 개의 네트워크에 포함되어있는 두 노드를 만나면 네트워크가 두 개가 됨.
def solution(n, computers):
    lst = []
    for row in range(n):
        S = set([col for col in range(n) if computers[row][col]])
        for i in range(len(lst)):
            if lst[i] & S:
                lst[i] |= S
                break
        else:
            lst.append(S)
    return len(lst)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))       # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))       # 1
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))       # 3
