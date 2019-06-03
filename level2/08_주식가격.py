def solution(prices):
    """
    # 효율성 테스트에서 오류남 O(n) 만들어야해
    ans = [0] * len(prices)
    for i, x in enumerate(prices):
        for y in prices[(i+1):]:
            ans[i] += 1
            if x > y:
                break
    """


    ans = [0] * len(prices)
    for i in range(len(prices)):
        ans[i] = sum(list(map(lambda y: 0 if prices[i] > y else 1, prices[i + 1:])))

    return ans
