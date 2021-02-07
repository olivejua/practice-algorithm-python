import collections
import sys

def solution(lst):
    graph = collections.defaultdict(list)
    for a, b in lst:
        graph[a].append(b)
        graph[b].append(a)

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
            a = queue.pop(0)
            for w in graph[a]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)
        return discovered

    dfs_result = dfs(1)
    bfs_result = bfs(1)
    print(len(dfs_result)-1)
    print(bfs_result)
    return

input = sys.stdin.readline
n = int(input())
m = int(input())

lst = []
for _ in range(m):
    lst.append(set(map(int, input().split())))

solution(lst)