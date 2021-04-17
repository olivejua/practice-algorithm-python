def solution(numbers, target):
    answer = list()
    length = len(numbers)

    def dfs(path: list):
        if len(path) == length:
            if sum(path) == target:
                answer.append(path)
            return

        dfs(path + [numbers[len(path)]])
        dfs(path + [-numbers[len(path)]])

    dfs(list())
    return len(answer)

def solution2(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution2(numbers[1:], target+numbers[0]) + solution2(numbers[1:], target-numbers[0])



# print(solution([1,1,1,1,1], 3))
print(solution2([1,1,1,1,1], 3))