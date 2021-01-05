"""
https://www.acmicpc.net/problem/5622
"""


while True:
    str = input()

    if str == '0':
        break

    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    time = 0

    for alpha in str:
        time += [idx+3 for idx, alphas in enumerate(dial) if alpha in alphas][0]
        print('alpha:', alpha, 'time:', time)

    print(time + len(str))

