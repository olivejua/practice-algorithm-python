import collections
import sys


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        if len(self.q) == 0:
            return -1

        return self.q.popleft()

    def size(self) -> int:
        return len(self.q)

    def empty(self) -> int:
        return 1 if len(self.q)==0 else 0

    def top(self) -> int:
        return self.q[0]


input = sys.stdin.readline
n = int(input())

stack = MyStack()
for _ in range(n):
    order = input().split()

    if order[0] == 'push':
        x = int(order[1])
        stack.push(x)
    elif order[0] == 'pop':
        print(stack.pop())
    elif order[0] == 'size':
        print(stack.size())
    elif order[0] == 'empty':
        print(stack.empty())
    elif order[0] == 'top':
        print(stack.top())