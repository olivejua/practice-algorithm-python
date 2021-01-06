# input = input()
# in_num1, in_num2 = input.split(" ")
#
# num1 = 0
# num2 = 0
# for idx, num in enumerate(in_num1):
#     num1 += (10 ** idx) * int(num)
#
# for idx, num in enumerate(in_num2):
#     num2 += (10 ** idx) * int(num)
#
# if num1 >= num2:
#     print(num1)
# else:
#     print(num2)


num1, num2 = input().split(" ")

num1 = ''.join(num1[::-1])
num2 = ''.join(num2[::-1])

if num1 >= num2:
    print(num1)
else:
    print(num2)