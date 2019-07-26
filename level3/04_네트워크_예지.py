'''
def solution(n, computers):
    lst =[]
    for row in range(n):
        S = set([col for col in range(n) if computers[row][col]])
        for i in range(len(lst)):
            if lst[i] & S:
                lst[i] |= S
                break
        else:
            lst.append(S)
    print(lst)
    return len(lst)

print(solution(5, [[1,1,0,1,0],[1,1,0,0,0],[0,0,1,0,1],[1,0,0,1,1],[0,0,1,1,1]]))
>[{0, 1, 2, 3, 4}, {2, 4}]
2

실제로는 하나의 네트워크라도
서로 직접 연결되지 않은 노드들이 먼저 나오면 새로운 네트워크를 만들어버려서 안 됨.
'''

#그냥 네가 올린 DFS 그대로 함
#computers에서 인덱스 안 가져오고 해보고 싶음

def solution(n, computers):
    answer = 1
    unvisit = list(range(len(computers)))
    stack = set([col for col in range(n) if computers[0][col]])

    while stack:
        node = stack.pop()
        if node in unvisit:
            unvisit.remove(node)
            stack.update([col for col in range(n) if computers[node][col]])
        if not stack and unvisit:
            answer += 1
            node = unvisit.pop()
            stack.update([col for col in range(n) if computers[node][col]])
    
    return answer
