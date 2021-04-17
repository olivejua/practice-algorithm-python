import collections


def solution(begin, target, words):
    if target not in words:
        return 0

    path = [begin]
    while words:
        print(path)
        if path[-1] == target:
            return path

        for i in range(len(target)):
            temp = path[-1]

            if temp[i] == target[i]:
                continue

            lst = list(temp)
            lst[i] = target[i]
            temp = ''.join(lst)
            print('temp=', temp)

            if temp in words:
                words.remove(temp)
                path.append(temp)
                break

    return path



solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])