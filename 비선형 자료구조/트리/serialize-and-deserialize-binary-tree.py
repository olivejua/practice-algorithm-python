# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([(root)])
        result = ['#']

        while queue:
            node = queue.popleft()
            # 부모 노드부터 하향식 스왑
            if node:
                queue.append(node.left)
                queue.append(node.right)
                # 결과 변수를 처리하는 부분
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data:str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root