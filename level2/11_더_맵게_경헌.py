import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        answer += 1
        t0 = heapq.heappop(scoville)
        if not scoville:
            if t0 < K: return -1
            else: break
        new = t0 + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)
    return answer
