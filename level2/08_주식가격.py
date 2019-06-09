def stock_price(prices_piece, ans, found_min_idx, idx_sup = 0):
    if len(prices_piece) == 0 or len(prices_piece) == 1:
        return

    # divide
    min_idx = prices_piece.index(min(prices_piece)) if not found_min_idx[idx_sup + len(prices_piece) - 1] else prices_piece.index(min(prices_piece[:-1]))
    past_prices = prices_piece[:min_idx + 1]
    future_prices = prices_piece[min_idx + 1:]

    # record the found min idx and answer
    found_min_idx[idx_sup + min_idx] = True
    ans[idx_sup + min_idx] = len(future_prices)

    # and conquer
    stock_price(past_prices, ans, found_min_idx, idx_sup)
    stock_price(future_prices, ans, found_min_idx, idx_sup + min_idx + 1)

    return

def solution(prices):
    """
    # 효율성 테스트에서 오류남 O(n) 만들어야해
    ans1 = [0] * len(prices)
    for i, x in enumerate(prices):
        for y in prices[(i+1):]:
            ans1[i] += 1
            if x > y:
                break
    """

    ans = [0] * len(prices)
    found_min_idx = [False] * len(prices)
    stock_price(prices, ans, found_min_idx)

    return ans

print(solution([1, 2, 3, 2, 3]))
print(solution([3, 2, 5, 1, 7, 2, 3, 8, 9, 11, 9, 5]))
