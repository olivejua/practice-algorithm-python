import sys

input = sys.stdin.readline
n = int(input())

a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

for x, y in sorted(a, key= lambda e: (e[0], e[1])):
    print(x, y)