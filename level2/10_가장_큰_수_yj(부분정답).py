#n이 m보다 앞에 오는 것이 더 큰 값인가?
def bigger(n, m):
    nm = n + m
    mn = m + n
    return True if nm > mn else False

def insertionSort(A):
    for i in range(1,len(A)):
        while 0 < i and bigger(A[i], A[i-1]):
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1

def solution(numbers):
    #insertionSort() 시간을 줄이기 위해
    #가장 긴 길이로 통일 후 sort
    #lenMax가 3이면, 12 -> 121
    #12와 121이 구분되지 않는 문제를 이후 insertionSort()로 보완
    strNumbers=[str(x) for x in numbers]
    lenMax = len(max(strNumbers, key=len))
    extension = [x + str(x[0])*(lenMax-len(x)) for x in strNumbers]
    extension_i = list(zip(extension, range(len(extension))))
    sorted_extension_i = sorted(extension_i, reverse = True)

    sorted_numbers = []
    for i in sorted_extension_i:
        sorted_numbers.append(strNumbers[int(i[1])])
        
    insertionSort(sorted_numbers)

    answer = ''
    for i in sorted_numbers:
        answer += i
    return answer