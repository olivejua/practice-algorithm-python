"""
삽입정렬
1. 인덱스별로 개수 세기
2. 직전 요소값 더하기
3. 아웃풋 배열 선언 (길이: input_array)
4. 인풋을 거꾸로 돌리며 값을 카운팅 인덱스로 검색하여 값이 아웃풋 인덱스로 가게하기. 카운팅 해당 인덱스는 -1
"""
import sys

input = sys.stdin.readline
n = int(input())

input_array = list()
for _ in range(n):
    input_array.append(int(input()))


counting_array = [0] * (max(input_array)+1)
for num in input_array:
    counting_array[num] += 1

for i in range(1, len(counting_array)):
    counting_array[i] += counting_array[i-1]

output_array = [-1] * len(input_array)

for num in input_array:
    index = counting_array[num] - 1
    output_array[index] = num
    counting_array[num] -= 1

print(*output_array, sep="\n")