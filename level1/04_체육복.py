def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 도난당한 경우 빌려줄 수 없음.
    tmp = []
    for r in reserve:
        for l in lost:
            if r == l:
                tmp.append(l)
                break
    for i in tmp:
        lost.remove(i)
        reserve.remove(i)

    # 여벌 체육복을 가져온 학생은 도난당하지 않았다는 가정 후 연산.
    borrow = []
    cont = False
    for r in reserve:
        tmp = []
        for l in lost:
            for i in borrow:
                if i[1] == l:
                    cont = True
            if cont:
                cont = False
                continue

            if r - 1 == l or r + 1 == l:
                tmp.append(r)
                tmp.append(l)
                borrow.append(tmp)
                break

    return n - len(lost) + len(borrow)
