def solution(n, stations, w):
    answer = 0
    S = set([i for s in stations for i in range(s - w, s + w + 1) if i > 0 and i < n + 1])
    """
    buildings = [i in S for i in range(1, n + 1)]

    width = 2 * w
    while buildings:
        building = buildings.pop()
        if not building:
            answer += 1
            buildings = buildings[:-width]
    """
    width = 2 * w
    tmp = 0
    for i in range(1, n + 1):
        if i in S:
            tmp = i
            continue
        if i > tmp:
            answer += 1
            tmp = i + width
    return answer

print(solution(11, [4, 11], 1)) # 3
print(solution(16, [9], 2)) # 3
