BOUNDARY = 5

def solution(dirs):
    d = 0
    p = [0, 0]
    routes = set()
    for move in dirs:
        route = p.copy()
        if move == 'U' and p[1] < BOUNDARY:
            p[1] += 1
        elif move == 'D' and p[1] > -BOUNDARY:
            p[1] -= 1
        elif move == 'R' and p[0] < BOUNDARY:
            p[0] += 1
        elif move == 'L' and p[0] > -BOUNDARY:
            p[0] -= 1
        
        if route == p: continue
        else:
            route = ' '.join(map(str, route + p))

            if route not in routes:
                routes.add(route)
                d += 1
    return d

print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))
