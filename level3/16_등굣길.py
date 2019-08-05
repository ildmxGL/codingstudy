def solution(m, n, puddles):
    route_present = [0] * (m + 1)
    route_past = [0] * (m + 1)

    route_present[1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if [x, y] == [1, 1]: continue
            if [x, y] in puddles:
                route_present[x] = 0
                continue
            route_present[x] = (route_present[x - 1] + route_past[x]) % 1000000007
        route_past = route_present.copy()
    return route_present[-1]

print(solution(4, 3, [[2, 2]]))
