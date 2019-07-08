"""
# 효율성 테스트 #1, #3 Failure
def solution(stock, dates, supplies, k):
    answer = 0
    today = 0
    while stock < k - today:
        idx = 0
        for i in range(len(dates)):
            if stock < dates[i] - today:
                break
            idx = i
        stock -= dates[idx] - today
        today = dates[idx]
        nextday = dates[idx+1] if idx+1 < len(dates) else k
        while stock < k - today and stock < nextday - today:
            maxidx = supplies.index(max(supplies[:idx+1]), 0, idx+1)
            dates.pop(maxidx)
            stock += supplies.pop(maxidx)
            idx -= 1
            answer += 1
    return answer
"""
import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    pq = []
    idx = 0
    len_dates = len(dates)
    for day in range(k):
        if day == dates[idx]:
            heapq.heappush(pq, -supplies[idx])
            idx += 1 if idx < len_dates - 1 else 0
        if not stock:
            stock = -heapq.heappop(pq)
            answer += 1
        stock -= 1
    return answer

print(solution(4, [4, 10, 15], [20, 5, 10], 30))            #2
print(solution(10, [5, 10], [1, 100], 110))                 #1
print(solution(5, [1, 2, 3, 4, 5], [1, 1, 1, 1, 25], 30))   #1
print(solution(4, [1, 2, 3, 4], [10, 40, 30, 20], 100))     #4
print(solution(4, [1, 2, 3, 4, 100], [10, 40, 30, 20, 50], 150))     #5

