m = input().split('-')
result = 0

for i in range(len(m)):
    p = list(map(int, m[i].split('+')))
    result = result-sum(p) if 0 < i else sum(p)

print(result)
