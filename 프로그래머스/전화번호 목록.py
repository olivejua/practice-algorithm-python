from typing import List


def solution(phone_book: List[str]):
    if len(phone_book) <= 1:
        return False

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j or len(phone_book[i]) < len(phone_book[j]):
                pass
            elif phone_book[j] in phone_book[i]:
                return False

    return True

def solution2(phone_book: List[str]):
    phone_book.sort()
    for a in range(len(phone_book)-1):
        if phone_book[a] in phone_book[a+1]:
            return False
    return True


print(len('119'))
print(solution(['119', '97674223', '1195524421']))
print(solution(['123', '456', '789']))
print(solution(['12', '123', '1235', '567', '88']))