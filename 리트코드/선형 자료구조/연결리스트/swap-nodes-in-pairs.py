class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs_mine(self, head: ListNode) -> ListNode:
        node = head

        prev = None
        while node:
            next = node.next

            if node.val%2 == 0:
                node.next = prev
                prev.next = next

            prev = node
            node = next

    def swapPairs_solution1(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head


    def swapPairs_solution2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)

        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head
            
            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음으로 이동
            head = head.next
            prev = prev.next.next

        return root.next

    def swapPairs_solution3(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값을 받음
            head.next = self.swapPairs_solution3(p.next)
            p.next = head
            return p
        return head