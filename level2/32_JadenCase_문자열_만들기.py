def solution(s):
    answer = []
    for x in s.split(' '):
        if not x:
            answer.append(x)
            continue
        answer.append(x[0].upper() + x[1:].lower() if x[0].isalpha() else x.lower())
    return ' '.join(answer)

print(solution("3people unFollowed me"))
print(solution("for the last week"))
