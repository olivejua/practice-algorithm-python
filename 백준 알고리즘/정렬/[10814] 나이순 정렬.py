import sys

input = sys.stdin.readline
n = int(input())

member = []
for _ in range(n):
    age, name = input().split()
    member.append((int(age), name))

for age, name in sorted(member, key= lambda x: x[0]):
    print(age, name)