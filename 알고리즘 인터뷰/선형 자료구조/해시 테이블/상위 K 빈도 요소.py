import collections
import heapq
from typing import List


class Solution:
    def topKFrequent_s1(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)

        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


    def topKFrequent_s2(self, nums: List[int], k: int):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

    print(topKFrequent_s2(None, [1,1,1,2,2,3], 2))



