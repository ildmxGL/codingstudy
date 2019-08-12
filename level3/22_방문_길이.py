BOUNDARY = 5

def solution(dirs):
    answer = 0
    p = [0, 0]
    routes = set()
    for move in dirs:
        p0 = p.copy()
        if move == 'U' and p[1] < BOUNDARY:
            p[1] += 1
        elif move == 'D' and p[1] > -BOUNDARY:
            p[1] -= 1
        elif move == 'R' and p[0] < BOUNDARY:
            p[0] += 1
        elif move == 'L' and p[0] > -BOUNDARY:
            p[0] -= 1
        
        if p0 == p: continue

        route = ' '.join(map(str, p0 + p))
        route_reverse = ' '.join(map(str, p + p0))
        if route not in routes:
            routes.add(route)
            routes.add(route_reverse)
            answer += 1
    return answer

print(solution('ULURRDLLU')) # 7
print(solution('LULLLLLLU')) # 7
