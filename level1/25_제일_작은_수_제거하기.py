def solution(arr):
    min_val = min(arr)
    return [-1] if len(arr) == 1 else [x for x in arr if x != min_val]
