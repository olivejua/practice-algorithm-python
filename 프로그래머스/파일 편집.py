import re


def solution(n, k, cmd):
    idxs = [1] * n

    deleted = []
    for c in cmd:
        if 'D' in c:
            go = re.findall("\d+", c)[0]
            steps = 0
            while steps < int(go):
                k+=1
                steps += idxs[k]
        elif 'U' in c:
            go = re.findall("\d+", c)[0]
            steps = 0
            while steps < int(go):
                k -= 1
                steps += idxs[k]
        elif 'C' == c:
            deleted.append(k)
            idxs[k] = 0
            k = k+1 if k!=n-1 else k-1
        elif 'Z' == c:
            idxs[deleted.pop()] = 1

    answer = ''
    for i in idxs:
        answer += 'O' if i == 1 else 'X'
    return answer

# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))