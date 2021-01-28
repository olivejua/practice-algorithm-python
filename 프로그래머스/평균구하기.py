def solution(arr):
    if len(arr) == 0:
        return 0

    return sum(arr)/len(arr)

print(solution([1,2,3,4]))