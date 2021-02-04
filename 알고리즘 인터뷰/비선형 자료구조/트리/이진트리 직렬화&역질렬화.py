# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        result = ['#']
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')

        return ''.join(result)

    def deserialize(self, data: str) -> TreeNode:
        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])

        index = 2
        while queue:
            node = queue.popleft()

            if nodes[index] is not '#':
                node.left = int(nodes[index])
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = int(nodes[index])
                queue.append(node.right)
            index += 1







# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))