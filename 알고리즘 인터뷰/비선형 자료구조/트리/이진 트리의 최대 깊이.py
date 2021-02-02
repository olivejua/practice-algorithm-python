import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()

                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)


        def dfs(node: TreeNode, depth: int):
            if not node:
                return

            depth += 1
            max_depth = max(max_depth, depth)
            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)
        return max_depth