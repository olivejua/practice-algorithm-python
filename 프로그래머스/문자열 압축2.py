'''
1. min 변수 생성 (결과값이 될것임)
2. 반복문 ( 1 ~ 전체길이/2). 이 단위로 문자열 자르기
3. 현재 자른 문자열을 다음 자른 문자열과 비교. 같은 문자열이 나오면 반복문 더 돌기. 다른 문자열 나오면 큐에 넣기.

5. min에 비교하여 저장하기
'''
import collections


def solution(s):
    answer = len(s)

    for cut in range(1, len(s)//2+1):
        print('======  cut=', cut, '  =======')

        result = ''
        temp = s[:cut]
        size = 0
        for idx in range(0, len(s), cut):
            if temp == s[idx:idx+cut]:
                size += 1
                if len(s)-1 < idx+cut:
                    result += (str(size)+temp)
            else:
                result += (str(size)+temp) if 1 < size else temp
                size = 1
                temp = s[idx:idx+cut]

                if len(s)-1 < idx+cut:
                    result += temp


        print('result=', result)
        answer = min(answer, len(result))

    return answer

print(solution('aabbaccc'))
# print(solution('abcabcdede'))
# print(solution('abcabcabcabcdededededede'))
# print(solution('ababcdcdababcdcd'))
#
# st = 'abcdefghijk'
# print(st[:])
# print(st[::2])