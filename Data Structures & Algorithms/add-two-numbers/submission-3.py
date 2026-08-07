# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 and l2:
            sums = l1.val + l2.val + carry
            carry = 0
            if sums >= 10:
                carry = 1
                sums -= 10
            curr.next = ListNode(sums)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sums = l1.val + carry
            if sums >= 10:
                carry = 1
                sums -= 10
            else:
                carry = 0
            curr.next = ListNode(sums)
            curr = curr.next
            l1 = l1.next
        while l2: 
            sums = l2.val + carry
            if sums >= 10:
                carry = 1
                sums -= 10
            else:
                carry = 0
            curr.next = ListNode(sums)
            curr = curr.next
            l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next
            

