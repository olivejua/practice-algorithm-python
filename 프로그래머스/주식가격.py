import collections


def solution(prices):
    answer = []

    for i in range(len(prices)):
        answer.append((len(prices)-1)-i)

    stack = []
    for i, price in enumerate(prices):
        while stack and price<stack[-1][0]:
            i_prev = stack.pop()[1]
            answer[i_prev] = i-i_prev
        stack.append((price, i))

    return answer


# d = collections.deque()
# d.append(1)
# d.append(2)
# d.append(3)
# for i in range(3):
#     print(i+1, d.pop())
# print(d[-1])
print(solution([1, 2, 3, 2, 3]))
