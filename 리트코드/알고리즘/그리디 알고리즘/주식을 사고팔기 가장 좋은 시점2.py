from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                result += prices[i+1]-prices[i]
        return result

    def maxProfit_s2(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))

    lst = [7,1,5,3,6,4]
    print(maxProfit(None, lst))