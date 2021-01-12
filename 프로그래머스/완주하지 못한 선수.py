import collections
from typing import List

class Solution:
    def solution(self, participant: List[str], completion: List[str]) -> str:
        p = collections.Counter(participant)
        for name in completion:
            p[name] -= 1

        return sorted(p.items(), key= lambda x: x[1])[-1][0]


    print(solution(None, ['leo', 'kiki', 'eden'], ['eden', 'kiki']))

    def solution2(self, participant, completion):
        participant.sort()
        completion.sort()
        for i in range(len(completion)):
            if participant[i] != completion[i]:
                return participant[i]
        return participant[-1]