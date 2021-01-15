n, k = map(int, input().split())
kinds = []

for _ in range(n):
    kinds.append(int(input()))

kinds.sort(reverse=True)

result = 0
for i in range(n):
    if k < kinds[i]:
        continue

    result += k // kinds[i]
    k -= kinds[i] * (k // kinds[i])

    # 0원이라면 더이상 연산하지 않도록 빠져나오기
    if not k:
        break

print(result)