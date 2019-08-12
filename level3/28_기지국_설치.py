def solution(n, stations, w):
    answer = 0
    p = 1
    width = 2 * w + 1
    for s in stations:
        i, j = s - w, s + w + 1
        if p < i:
            answer += (i - p - 1) // width + 1
        p = j
    else:
        if p <= n:
            answer += (n + 1 - p - 1) // width + 1
    return answer

print(solution(11, [4, 11], 1)) # 3
print(solution(16, [9], 2)) # 3
print(solution(11, [4, 5, 11], 1)) # 2
