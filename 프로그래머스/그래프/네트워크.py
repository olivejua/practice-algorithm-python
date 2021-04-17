import collections


def solution(n, computers):
    answer = 0
    visited = []

    def bfs(start):
        queue = collections.deque()
        queue.append(start)

        while queue:
            num = queue.popleft()
            visited.append(num)
            queue += [i for i, c in enumerate(computers[num]) if c == 1 and i not in visited]

    for com in range(n):
        if com not in visited:
            answer += 1
            bfs(com)

    return answer



print(solution(3, [[1,1,0], [1,1,0], [0,0,1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

networks = [
    [1, 1, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]
print(solution(5, networks))

networks = [
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1]
]
print(solution(4, networks))
networks = [
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 1]
]
print(solution(4, networks))