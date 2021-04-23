import collections


'''
균형잡힌 문자열 : 괄호 개수가 맞음
올바른 문자열 : 괄호 개수 + 짝도 맞음

1. 올바른 문자열인지 확인
    1-Y: return 문자열 그대로
2. 재귀 호출

[재귀호출]
1. 빈 문자열인지 확인
    1-Y. 빈 문자열 리턴
2. result 변수 선언
3. u, v 변수 선언
4. 첫번째 괄호부터 균형잡힌 문자열이 되자마자 u에 저장, 나머지 v에 저장
5. u가 올바른 문자열인지 확인
    5-Y. 
        1. result+=u 
        2. result+=재귀호출(v)
        3. result 리턴
    5-N. 
        1. result+='('
        2. result+=재귀호출(v)
        3. result+=')'
        4. u = u[1:len(u)-1:-1]
        5. result+=u
        6. result 리턴


'''

def solution(p):
    def change(w):
        if not w:
            return w

        u = v = ''

        balanced = 0
        for i in range(len(w)):
            if w[i] == '(':
                balanced += 1
            elif w[i] == ')':
                balanced -= 1

            if balanced == 0:
                u, v = w[:i+1], w[i+1:]
                break
        print(u, v)

        if isRightStr(u):
            return u + change(v)
        else:
            result = '('
            result += change(v)
            result += ')'
            # result += u[len(u)-2:0:-1]

            for l in u[1:len(u)-1]:
                if l == '(':
                    result += ')'
                else:
                    result += '('

            return result

    return change(p)


def isRightStr(s):
    stack = []

    for l in s:
        if l == '(':
            stack.append(l)
        else:
            if not stack:
                return False
            stack.pop()

    return True

# print(solution('()))((()'))
print(solution('))((()'))