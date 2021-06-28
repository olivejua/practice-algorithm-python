import collections


def solution(n, edge):
    graph = dict()

    for i in range(n):
        graph[i+1] = []

    visited = collections.defaultdict(int)

    # 인접리스트로 구성
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    Q = collections.deque([(1, 0)])
    while Q:
        node, cnt = Q.popleft()

        for n in graph[node]:
            if visited[n]:
                visited[n] = min(visited[n], cnt+1)
            else:
                visited[n] = cnt+1
                Q.append((n, cnt+1))

    return sum([1 for k, v in visited.items() if v == max(visited.values()) and k != 1])


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))