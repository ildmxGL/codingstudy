def solution(s):
    l = s.split(' ')
    ans = []
    for i, x in enumerate(l):
        tmp = ''
        for j, y in enumerate(list(x)):
            if not y.isalpha():
                tmp += y
                continue

            if j % 2 == 0:
                tmp += chr(ord(y) - (ord('a') - ord('A'))) if y.islower() else y
            else:
                tmp += chr(ord(y) + (ord('a') - ord('A'))) if y.isupper() else y

        ans.append(tmp)

    return ' '.join(ans)
