"""
# 예지 풀이
def bigger(n, m):
    nm = n + m
    mn = m + n
    return True if nm > mn else False

def insertionSort(A):
    for i in range(1, len(A)):
        while 0 < i and bigger(A[i], A[i-1]):
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1

def solution(numbers):
    print(numbers)
    strNumbers = [str(x) for x in numbers]
    lenMax = len(max(strNumbers, key = len))
    extension = [x + str(x[0]) * (lenMax - len(x)) for x in strNumbers]
    extension_i = list(zip(extension, range(len(extension))))
    sorted_extension_i = sorted(extension_i, reverse = True)

    sorted_numbers = []
    for i in sorted_extension_i:
        sorted_numbers.append(strNumbers[int(i[1])])
    insertionSort(sorted_numbers)

    answer = ''
    for i in sorted_numbers:
        answer += i
    return str(int(answer))
"""
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x * 3, reverse = True)
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0]))
print(solution([0, 1000, 0, 0]))
print(solution([12, 121]))
print(solution([21, 212]))
print(solution([5, 546]))
