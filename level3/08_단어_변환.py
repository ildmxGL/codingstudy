def solution(begin, target, words):
    answer = 51
    n = len(begin)
    stack = []
    visited = []
    
    stack.append([begin, 0])
    while stack:
        node = stack.pop()

        if node[0] == target:
            answer = min(node[1], answer)

        visited = visited[:node[1]]
        visited.append(node[0])

        nexts = []
        for word in words:
            c = sum([1 for i in range(n) if word[i] != node[0][i]])
            if c != 1 or word in visited:
                continue
            cont = False
            for x in stack:
                if word == x[0]:
                    cont = True
            if cont:
                continue

            nexts.append([word, node[1] + 1])
        stack.extend(nexts)
    return answer if answer != 51 else 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))   # 4
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))          # 0
