pick = int(input())

turn = 0
limit = 1
while limit < pick:
    turn = turn + 1
    limit = limit + (6 * turn)

print(turn + 1)