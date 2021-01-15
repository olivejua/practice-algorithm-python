import collections

# n = int(input())
# schedules = collections.defaultdict(list)
# for _ in range(n):
#     start, end = map(int, input().split())
#     schedules[start].append(end)

# max_cnt = 0
# for key in sorted(schedules):
#     cnt = 0
#     start = key
#     while start <= max(schedules.keys()):
#         cnt += 1
#
#         # 끝나는 시간에 정확히 시작하는 시간이 없을 때 다음키가 존재할 때까지
#         if start not in schedules:
#             for i in range(start+1, max(schedules.keys())+1):
#                 if i in schedules:
#                     start = i
#                     break
#         start = schedules[start][0]
#     max_cnt = max(max_cnt, cnt)
#
# print(max_cnt)

import sys

input = sys.stdin.readline
n = int(input())
schedules = []
for _ in range(n):
    start, end = map(int, input().split())
    schedules.append((start, end))

schedules.sort(key= lambda x: (x[1], x[0]))

meetings = 0
end = 0
for i in range(n):
    start = schedules[i][0]
    if end <= start:
        meetings += 1
        end = schedules[i][1]

print(meetings)
