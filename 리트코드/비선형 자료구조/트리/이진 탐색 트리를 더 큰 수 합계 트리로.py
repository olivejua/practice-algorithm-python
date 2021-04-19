"""
leetcode: binary-search-tree-to-greater-sum-tree
BST의 각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    val: int = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중회 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root