from typing import List


def solution1(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    # left_max, right_max = 0, 1

    # 7 < 8
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # left_max(3), right_max(2) = max(3, 2), max(1, 2)
        # 더 높은 쪽을 향해 투 포인트 이동
        # 3 <= 2
        if left_max <= right_max:
            volume += left_max - height[left]
            # volume(5) += 2 - 1
            left += 1
            # 7
        else:
            volume += right_max - height[right]
            # volume(1) += 2 - 1
            right -= 1
            # 8
    return volume


def solution2(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break
            
            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume