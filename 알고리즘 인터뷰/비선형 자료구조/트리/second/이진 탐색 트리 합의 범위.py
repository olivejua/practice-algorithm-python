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
                dfs(node.right)
            elif R < node.val:
                dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)