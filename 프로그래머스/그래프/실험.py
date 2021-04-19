import collections

# letters = [char for char in str1 if char not in str2]

word = 'cog'
word2 = 'hit'
stack = collections.deque()

index = 2
str1 = word2[:index] + word[index] + word2[index+1:]

print(str1)