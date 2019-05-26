def ans1(num):
    answer_pattern = [1, 2, 3, 4, 5]
    num %= len(answer_pattern)
    return answer_pattern[num]

def ans2(num):
    answer_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    num %= len(answer_pattern)
    return answer_pattern[num]

def ans3(num):
    answer_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num %= len(answer_pattern)
    return answer_pattern[num]

def solution(answers):
    answer = []
    count1 = 0
    count2 = 0
    count3 = 0

    for idx, val in enumerate(answers):
        if ans1(idx) == val:
            count1 += 1
        if ans2(idx) == val:
            count2 += 1
        if ans3(idx) == val:
            count3 += 1

    max_val = 0
    if count1 > max_val:
        max_val = count1
    if count2 > max_val:
        max_val = count2
    if count3 > max_val:
        max_val = count3

    if max_val == count1:
        answer.append(1)
    if max_val == count2:
        answer.append(2)
    if max_val == count3:
        answer.append(3)

    return answer

# ------------- solution 함수 테스트 ------------- 
result = solution([1,2,3,4,5])
print(result)

result = solution([1,3,2,4,2])
print(result)
# ------------------------------------------------ 
