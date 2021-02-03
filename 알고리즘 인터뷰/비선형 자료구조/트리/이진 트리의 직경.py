"""
가장 긴 노드를 출력하라
상태값 누적 트리
leetcode: diameter-of-binary-tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2)
            return max(left, right)+1

        dfs(root)
        return self.longest