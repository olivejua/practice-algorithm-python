import collections
import heapq
from typing import List

'''
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

1. 힙 리스트 변수를 만든다.
while문
2. 스코빌 오름차순 정렬 (힙에다 저장)
3. 앞 2개 뽑아서 K보다 작은지 비교한다.
4. 낮으면 제시한 방법으로 연산해서 힙에 저장 
'''
def solution(scoville, K):
    answer = 0
    heap = list()

    for food in scoville:
        heapq.heappush(heap, food)

    while heap[0] < K:
        try:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            heapq.heappush(heap, first + (second*2))
        except IndexError:
            return -1
        answer+=1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))

# s = [0, 0]
# if not s:
#     print('not s')
# else:
#     print('s')
#     print(set(s).pop() == 0)
