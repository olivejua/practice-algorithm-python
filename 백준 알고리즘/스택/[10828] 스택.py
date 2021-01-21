import collections
import sys


class Stack:
    def __init__(self):
        self.stack = collections.deque()
        self.size:int = 0

    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1

        self.size -= 1
        return self.stack.pop()

    def empty(self) -> int:
        return 1 if self.size==0 else 0

    def top(self) -> int:
        if self.size == 0:
            return -1

        x = self.stack.pop()
        self.stack.append(x)

        return x


input = sys.stdin.readline

n = int(input())

stack = Stack()
for _ in range(n):
    order = input()

    if 'push' in order:
        x = int(order.split()[1])
        stack.push(x)
    elif 'pop' in order:
        print(stack.pop())
    elif 'size' in order:
        print(stack.size)
    elif 'empty' in order:
        print(stack.empty())
    elif 'top' in order:
        print(stack.top())