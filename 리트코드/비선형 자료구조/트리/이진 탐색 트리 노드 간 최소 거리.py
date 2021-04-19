"""
leetcode: minimum-distance-between-bst-nodes
두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.
"""
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST_mine(self, root: TreeNode) -> int:
        left = 0
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            right = dfs(node.right)

            if right == 0:
                self.left = node.val
            return 1

        dfs(root.left)

        return min(root.val - left, root.right.val - root.val)

    def minDiffInBST_s1(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST_s1(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST_s1(root.right)

        return self.result

    def minDiffInBST_s2(self, root: TreeNode) -> int:
        stack = []
        node = root

        # 반복 구조 중위 준회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - self.prev)
            self.prev = node.val

            node = node.right

        return result