import sys

input = sys.stdin.readline
n = int(input())

people = list(map(int, input().split()))
people.sort()

result = []
for person in people:
    if result:
        result.append(result[-1] + person)
    else:
        result.append(person)

print(sum(result))