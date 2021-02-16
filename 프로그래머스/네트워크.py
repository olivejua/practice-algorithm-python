import collections


# def solution(n, computers):
#     networks = 0
#     queue = []
#
#     while queue:
#         com = queue.pop()
#         for i in range(n):
#             if computers[i][com] == 1:
#                 for j in range(n):
#
#
#
# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#
# for i in range(n):
#     for j in range(n):
#         print(i, j, computers[i][j])
#         if computers[i][j] == 1:
#             print(True)