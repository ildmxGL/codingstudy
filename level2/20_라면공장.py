import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    pq = []
    idx = 0
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(pq, -supplies[i])
                idx = i + 1
            else:
                break
        stock -= heapq.heappop(pq)
        answer += 1
    return answer
    
print(solution(4, [4, 10, 15], [20, 5, 10], 30))            #2
print(solution(10, [5, 10], [1, 100], 110))                 #1
print(solution(5, [1, 2, 3, 4, 5], [1, 1, 1, 1, 25], 30))   #1
print(solution(4, [1, 2, 3, 4], [10, 40, 30, 20], 100))     #4
print(solution(4, [1, 2, 3, 4, 100], [10, 40, 30, 20, 50], 150))     #5

