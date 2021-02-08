from typing import List


def solution(numbers, target):
    result = []

    def dfs(index: int, stack: List):
        if len(stack) == len(numbers):
            if sum(stack) == target:
                result.append(stack)
            return 0

        dfs(index+1, stack + [numbers[index]])
        dfs(index+1, stack + [-numbers[index]])

    dfs(-1, [])
    return len(result)

def solution_dfs(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0

    return solution_dfs(numbers[1:], target + numbers[0]) + \
           solution_dfs(numbers[1:], target - numbers[0])


print(solution_dfs([1,1,1,1,1], 3))