n = int(input())

result = 0
for i in range(1, n+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if n == sum_num:
        result = i
        break

print(result)