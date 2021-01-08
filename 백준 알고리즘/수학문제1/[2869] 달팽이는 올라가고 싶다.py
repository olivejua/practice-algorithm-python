A, B, V = map(int, input().split())

cur, days = 0, 0
# while cur < V:
#     print(cur)
#     days += 1
#     cur += A
#     if cur == V:
#         break
#     cur -= B

Is = 0
if (V-B) % (A-B) != 0:
    Is = ((V-B)//(A-B)) + 1
else:
    Is = ((V-B) // (A-B))

print(Is)