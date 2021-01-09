def solution(n, m)-> int:
    cards = list(map(int, input().split()))
    cards.sort()

    result = 0
    for i in range(n-2):
        left, right = i+1, len(cards)-1
        while left < right:
            sum = cards[i]+cards[left]+cards[right]
            if m == sum:
                return sum
            elif m < sum:
                right -= 1
            else: # sum < m
                if result < sum:
                    result = sum
                    print(cards[i], cards[left], cards[right], result, m-result)
                left += 1
            print('허탕')
    return result

n, m = map(int, input().split())
print(solution(n, m))