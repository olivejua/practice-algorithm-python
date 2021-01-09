import math


def is_prime(num:int) -> bool:
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def solution(n):
    answer = 0

    if n == 1:
        return 0
    elif n == 2:
        return 1

    for num in range(2, n+1):
        if is_prime(num):
            answer += 1

    return answer


def better_solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)