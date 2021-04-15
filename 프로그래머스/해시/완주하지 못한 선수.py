import collections
from typing import List


def solution(participant: List[str], completion: List[str]):
    hash = collections.Counter(participant)

    for p in completion:
        if p in hash and hash[p] > 0:
            hash[p] -= 1

    for p in hash:
        if hash[p] > 0:
            return p

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))