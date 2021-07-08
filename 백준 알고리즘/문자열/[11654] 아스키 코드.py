import sys

input = sys.stdin.readline

alpha_big = ['A', 'B', 'C', 'D', 'E',
             'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

alpha_small = ['a', 'b', 'c', 'd', 'e',
               'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']

v = str(input()).rstrip('\n')

if alpha_big.__contains__(v):
    print(alpha_big.index(v)+65)
elif alpha_small.__contains__(v):
    print(alpha_small.index(v)+97)
else:
    v = int(v)
    print(v+48)