class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 재귀 구조
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1이 존재하지 않거나 있어도 l1이 l2보다 큰 경우 뒤바꾸기
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        #
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1