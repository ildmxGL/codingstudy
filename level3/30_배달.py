import heapq

def solution(N, road, K):
    dist = dict()
    Q = []
    visited = set()

    dist[1] = 0

    for node in range(1, N + 1):
        if node != 1:
            dist[node] = float('inf')
        heapq.heappush(Q, (dist[node], node))
        
    while Q:
        p, u = heapq.heappop(Q)

        for idx, r in enumerate(road):
            if idx in visited or u not in r[:2]:
                continue

            v = r[0] if r[0] != u else r[1]
            alt = dist[u] + r[2]
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(Q, (dist[v], v))
            visited.add(idx)
            
    return sum(i <= K for i in dist.values())

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))               # 4
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))    # 4
