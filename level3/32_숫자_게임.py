def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)

    i = 0
    for a in A:
        if B[i] > a:
            answer += 1
            i += 1
    
    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
