n, m = map(int, input().split())

result = []
def dfs(idx: int, current: list):
    if m == len(current):
        result.append(current)
        return

    for i in range(idx, n+1):
        print('i=', i)
        current.append(idx)
        dfs(i, current[:]+[i])


dfs(1, [])
print(result)