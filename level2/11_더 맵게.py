import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer=0
    while scoville[0] < K:
        answer += 1
        new = heapq.heappop(scoville)+heapq.heappop(scoville)*2
        heapq.heappush(scoville, new)
    return answer

'''
정확성 테스트 1,3,8,14 런타임에러
'''
