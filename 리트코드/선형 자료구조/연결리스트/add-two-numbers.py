from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 연결리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬리스트로 변환
    def toList(self, node: ListNode) -> ListNode:
        list: List = []

        while node:
            list.append(node)
            node = node.next

        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

    # 두 연결리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(map(str, a))) + \
                    int(''.join(map(str, b)))

        return self.toReversedLinkedList(str(resultStr))





class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(carry+sum, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next