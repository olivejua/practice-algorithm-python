m, n = int(input()), int(input())
prime_nums = []
for num in range(m, n+1):
    if num==1:
        pass
    elif num==2:
        prime_nums.append(num)
    else:
        for i in range(2, num):
            if num % i == 0:
                break
            elif num-1==i:
                prime_nums.append(num)

if 1 <= len(prime_nums):
    print('{}\n{}'.format(sum(prime_nums), min(prime_nums)))
else:
    print(-1)
