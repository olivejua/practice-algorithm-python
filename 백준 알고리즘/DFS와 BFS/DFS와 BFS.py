import collections
import sys


def solution(lst, v):
    graph = collections.defaultdict(list)
    for a, b in lst:
        graph[a].append(b)
        graph[b].append(a)
    
    # 작은 수부터 탐방
    for key in graph.keys():
        graph[key].sort()

    def dfs(v, discovered=[]):
        discovered.append(v)
        for w in graph[v]:
            if w not in discovered:
                discovered = dfs(w, discovered)
        return discovered

    def bfs(v):
        discovered = [v]
        queue = [v]
        while queue:
            v = queue.pop(0)
            for w in graph[v]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered

    dfs_result = dfs(v)
    bfs_result = bfs(v)

    print(' '.join(map(str, dfs_result)))
    print(' '.join(map(str, bfs_result)))

    return


input = sys.stdin.readline

# n: 정점의 개수, m: 간선의 개수, v: 탐색 시작 번호
n, m, v = map(int, input().split())
lst = []
for _ in range(m):
    a, b = map(int, input().split())
    lst.append((a,b))
solution(lst, v)