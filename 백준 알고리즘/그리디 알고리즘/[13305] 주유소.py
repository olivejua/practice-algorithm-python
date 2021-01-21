import sys

input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

cost = price[0]*dist[0]
min_p = price[0]
for i in range(1, len(price) - 1):
    min_p = min(min_p, price[i])
    cost += min_p*dist[i]

print(cost)