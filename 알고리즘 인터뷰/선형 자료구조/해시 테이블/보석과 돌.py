import collections


class Solution:
    def numJewelsInStones_s1(self, J: str, S: str) -> int:
        fregs = {}
        count = 0

        for char in S:
            if not char in fregs:
                fregs[char] = 1
            else:
                fregs[char] += 1

        for char in J:
            if char in fregs:
                count += fregs[char]

        return count


    def numJewelsInStones_s2(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # 비교 없이 돌(S) 빈도 수 계산
        for char in S:
            freqs[char] += 1

        # 비교 없이 보석(J) 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count


    def numJewelsInStones_s3(self, J: str, S: str) -> int:
        fregs = collections.Counter(S)
        count = 0

        for char in J:
            count += fregs[char]

        return count

    def numJewelsInStones_s4(self, J: str, S: str) -> int:
        return sum (s in J for s in S)

    #
    # def numJewelsInStones_mine(self, J: str, S: str) -> int:
    #     count = 0
    #
    #     for char in S:
    #         if char in J:
    #             count += 1
    #
    #     return count