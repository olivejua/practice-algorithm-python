import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = groupAnagrams(strs)
print(anagrams)

a = 'zbdaf'
print(''.join(sorted(a)))

c = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(c, key=len))

a = ['cde', 'cfc', 'abc']

print(sorted(a, key=lambda s: (s[0], s[-1])))