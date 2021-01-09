def countdown(n):
    if n<=0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)
        countdown(n-2)
        print(n)

countdown(10)

def draw_star(n):
    global Map

    if n==3:
        Map[0][:3] = Map