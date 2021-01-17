import sys

str = sys.stdin.readline()
equation = []

for char in str:
    if char.isalnum():
        if equation and type(equation[-1]) == int:
            equation.append(equation[-1] + (int(char)*10))
        else:
            print(char)
            equation.append(int(char))
    else:
        equation.append(char)

print(equation)
