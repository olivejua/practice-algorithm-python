def solution1(arr):
    answer = []

    if not arr:
        return answer

    answer.append(arr[0])
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer

def solution2(a, b):
    if a > b:
        a, b = b, a

    return sum(range(a, b+1))

lst = [1,1,3,3,0,1,1]
print(solution1(lst))

print(solution2(5, 3))