fixed, variable, sales = map(int, input().split())

if sales <= variable:
    print(-1)
else:
    print((fixed // (sales-variable))+1)