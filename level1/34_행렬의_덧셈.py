def solution(arr1, arr2):
    ans = []
    for i, x in enumerate(arr1):
        e = [a + arr2[i][j] for j, a in enumerate(x)]
        ans.append(e)
    return ans
