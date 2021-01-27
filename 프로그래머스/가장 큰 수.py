def isSwitch(num1: int, num2: int) -> bool:
    return str(num1)+str(num2) < str(num2)+str(num1)

def solution(numbers):
    i = 1
    while i < len(numbers):
        j = i
        while 0 < j and isSwitch(numbers[j-1], numbers[j]):
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            j -= 1
        i += 1

    return str(int(''.join(map(str, numbers))))

print(solution([6,10,2]))
print(solution([3,30,34,5,9]))