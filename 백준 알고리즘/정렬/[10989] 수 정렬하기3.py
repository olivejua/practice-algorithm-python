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

input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

for n in counting_sort(a):
    print(n)
