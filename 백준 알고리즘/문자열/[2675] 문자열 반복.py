"""
https://www.acmicpc.net/problem/2675
"""



t = int(input())

for _ in range(t):
    s = input()
    r, letters = s.split(" ")

    p = ''.join(l*r for l in letters)

    print(p)