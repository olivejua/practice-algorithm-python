import collections
import re


def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')
    print(s1)

    lst = []
    for i in s1:
        lst.append(i.split(","))

    lst.sort(key=len)

    for i in lst:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))

    return answer


def solution2(s):
    s = collections.Counter(re.findall('\d+', s))

    return list(map(int, [k for k, v in sorted(s.items(), key= lambda x: x[1], reverse=True)]))

a = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
b = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
c = "{{123}}"
d = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
e = "{{20,111},{111}}"
# print(solution2(a))
print(solution(b))
# print(solution(c))
# print(solution2(d))
# print(solution(e))
