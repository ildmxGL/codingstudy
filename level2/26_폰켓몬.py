def solution(nums):
    N_half = len(nums) // 2
    num = len(set(nums))
    return N_half if num > N_half else num

print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
