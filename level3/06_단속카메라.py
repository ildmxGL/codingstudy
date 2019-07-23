def solution(routes):
    answer = 0
    routes.sort()
    idx = 0
    while True:
        intersection = [-30000, 30000]
        answer += 1
        for i, route in enumerate(routes[idx:]):
            if route[0] <= intersection[1]:
                intersection[0] = max(route[0], intersection[0])
                intersection[1] = min(route[1], intersection[1])
            else:
                idx += i
                break
        else:
            break
    return answer

print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))               # 2
print(solution([[-2, -1], [1, 2], [-3, 0]]))                                # 2
print(solution([[0, 0], ]))                                                 # 1
print(solution([[0, 1], [0, 1], [1, 2]]))                                   # 1
print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))                           # 4
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))              # 2
print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))               # 2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))   # 2
