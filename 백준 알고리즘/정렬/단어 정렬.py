import sys

n = int(sys.stdin.readline().rstrip())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

words = set(words)
for word in sorted(words, key=lambda x: (len(x), x)):
    sys.stdout.write(word + "\n")