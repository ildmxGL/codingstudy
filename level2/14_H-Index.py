import heapq

def solution(citations):
    c = []
    while citations:
        heapq.heappush(c, citations.pop())

    idx = 0
    l = len(c)
    while True:
        if idx == l or heapq.heappop(c) >= l - idx:
            break
        idx += 1

    return l - idx

print(solution([3, 0, 6, 1, 5]))
print(solution([10, 8, 5, 4, 3]))
print(solution([25, 8, 5, 3, 3]))
