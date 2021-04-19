import collections


def solution(tickets):
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))

        route.append(a)

    dfs('ICN')

    return route

print('path=', solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print('path=', solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))