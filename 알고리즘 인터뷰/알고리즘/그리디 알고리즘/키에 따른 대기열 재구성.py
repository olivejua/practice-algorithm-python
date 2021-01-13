import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []

        while heap:
            person = heapq.heappop(heap)
            print(person)
            result.insert(person[1], [-person[0], person[1]])

        print(result)
        return result

    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    reconstructQueue(None, people)