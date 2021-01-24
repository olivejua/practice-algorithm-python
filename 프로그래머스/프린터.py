import collections


def solution(priorities, location):
    answer = 0
    d = collections.deque((v, i) for i, v in enumerate(priorities))

    print(d)
    while len(d):
        J = d.popleft()
        if d and max(d)[0] > J[0]:
            d.append(J)
        else:
            answer += 1
            if J[1] == location:
                break

    return answer


print(solution([2,1,3,2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))