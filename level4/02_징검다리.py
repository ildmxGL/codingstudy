def solution(distance, rocks, n):
    BEGIN = 0
    END = distance
    rocks.sort()
    ds = []

    for i in range(0, n + 1):
        d = 0
        if i == len(rocks):
            d = END - rock
        elif i > len(rocks):
            continue
        else:
            d = rock - BEGIN
        ds.append([-1, i, d])
    for i_r in range(len(rocks)):
        for i in range(i_r + 1, i_r + n + 2):
            d = 0
            elif i == len(rocks):
                d = END - rocks[i_r]
            elif i > len(rocks):
                continue
            else:
                d = rocks[i] - rocks[i_r]
            ds[i_r].append(d)
        else:
            ds[i_r].sort(key x: x[2])
    

   

    answer = 0

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
