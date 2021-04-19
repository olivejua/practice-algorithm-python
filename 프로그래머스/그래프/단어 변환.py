import collections

"""
while문 로직
1. stack에 target이 포함되어 있는지 확인
    1-yes. while문 종료
2. stack에서 단어(word) 하나를 꺼낸다.
3. 꺼내면 stack 비움 (word에 맞춘 새로운 후보들을 넣어야하니까)
4. for문을 target 길이 수만큼 실행한다.
    4-1. word 글자에서 현재 반복문 인덱스의 target 자리의 문자를 word 글자에 덮어씌워 교체한다.
    4-2. words에 있는지 확인한다.
    4-3. stack에 넣는다.

"""
def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0

    stack = collections.deque()
    stack.append(begin)

    while stack:
        if target in stack:
            break

        word = stack.pop()
        print('word=', word, 'stack=', stack)
        stack.clear()

        for i in range(len(target)):
            temp = word[:i] + target[i] + word[i+1:]

            if temp in words:
                stack.append(temp)
                words.remove(temp)

            print('temp=', temp, 'stack=', stack, 'words=', words)

        answer += 1

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))