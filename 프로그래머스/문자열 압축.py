import math


def solution(s):
    if len(s) == 1:
        return 1

    min_length = 0
    result = ''

    for cut in range(1, len(s)//2 + 1):
        count = 1
        tempStr = s[:cut]

        for i in range(cut, len(s), cut):
            print("==" + s[i] + "==")

            if tempStr == s[i:i+cut]:
                count += 1
            else:
                if count == 1:
                    count = ""

                result += str(count) + tempStr
                tempStr = s[i:i+cut]
                count = 1

            if count == 1:
                count = ""
            result += str(count) + tempStr
            min_length = min(min_length, len(result))

    return min_length

print(solution('abcabcdd'))