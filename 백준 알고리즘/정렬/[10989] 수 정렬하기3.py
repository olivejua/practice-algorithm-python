import sys


def counting_sort(a):
    max_num = max(a)
    aux = [0 for _ in range(len(a))]
    c = [0 for _ in range(max_num+1)]

    # 각 원소 갯수 계산
    for i in range(len(a)):
        c[a[i]] += 1

    # 누적합 계산
    for i in range(1, len(c)):
        c[i] += c[i-1]

    # 누적합을 이용해 정렬 (a는 내림차순으로 조회)
    for i in range(1, len(a)+1):
        c[a[-i]] -= 1
        aux[c[a[-i]]] = a[-i]

    return aux

n = int(sys.stdin.readline())
b = [0] * 10001
for i in range(n):
    b[int(sys.stdin.readline())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)