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
