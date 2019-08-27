def solution(phone_book):
    phone_book.sort()
    for x, y in zip(phone_book, phone_book[1:]):
        if x == y[:len(x)]:
            return False
    return True

'''
다른 사람 풀이
startswith() 사용

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
'''