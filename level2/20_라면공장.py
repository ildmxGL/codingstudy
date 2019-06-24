from collections import deque

def solution(stock, dates, supplies, k):
    if k <= stock:
        return 0
    plant = deque([x for x in zip(dates, supplies)])

    answer = 0
    today = 0
    while stock < k - today:
        tmp = deque()
        # stock으로 언제까지 버틸 수 있을지 찾기
        while plant:
            supply = plant.popleft()
            if supply[0] - today > stock:
                plant.appendleft(supply)
                break
            tmp.append(tmp)

        # 찾은 supplies 중에서 

        stock += tmp[1] - (tmp[0] - today)
        today = tmp[0]
        answer += 1

    return answer

print(solution(4, [4, 10, 15], [20, 5, 10], 30))
