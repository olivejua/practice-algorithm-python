"""
leetcode: range-sum-of-bst
이진 탐색 트리(BST)가 주어졌을 때 L 이상 R 이하의 값을 지닌 노드의 합을 구하라.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST_s1(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        return (root.val if L <= root.val <= R else 0) + \
            self.rangeSumBST(root.left, L, R) + \
            self.rangeSumBST(root.right, L, R)

    def rangeSumBST_s2(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)

            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

    def rangeSumBST_s3(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0

        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val

        return sum