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

    def topKFrequent_s2(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


    def topKFrequent_mine(nums: List[int], k: int) -> List[int]:
        freqs = collections.defaultdict(int)
        answer = []

        for num in nums:
            freqs[num] += 1

        answer = sorted(freqs.items(), reverse=True, key=lambda item:item[1])

        for key in freqs.keys():
            answer.append(key)

        print(freqs)

        return answer


l = [1,2]
k = 2
s = Solution
print(s.topKFrequent_mine(l, k))
    # print(topKFrequent_s1())

# solution = Solution
