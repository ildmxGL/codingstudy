import itertools

def solution(numbers):
    """
    # permutation을 사용하여 굉장히 비효율적인 코드.
    return str(int(max(list(map(lambda x: ''.join(map(str, x)), itertools.permutations(numbers))))))
    """

    print(numbers)
    ans = ''
    while len(numbers):
        numbers = sorted(map(str, numbers), key = lambda num: num[0], reverse = True)

        cands = [x for x in numbers if x[0] == numbers[0][0]]
        numbers = numbers[len(cands):]

        ans += max(list(map(lambda x: ''.join(x), itertools.permutations(cands))))

    return str(int(ans))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0]))
print(solution([0, 1000, 0, 0]))
print(solution([12, 121]))
print(solution([21, 212]))
print(solution([5, 546]))
