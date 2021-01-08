for _ in range(int(input())):
    h, w, n = map(int, input().split())

    floor = (n%h)*100 if n%h!=0 else h*100
    room = (n//h)+1 if n%h!=0 else (n//h)
    print(floor+room)
