from typing import List


def reverseString(s: List[str]) -> None:
    s[:] = s[::-1]

    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)


reverseString(["h", "e", "l", "l", "o"])