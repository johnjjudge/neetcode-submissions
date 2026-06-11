# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        # find the length of the list
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        # calculate index to remove
        indexToRemove = length - n

        # if its the first elem
        if indexToRemove == 0:
            return head.next

        # other wise remove the ith elem
        i = 0
        curr = head
        while i < indexToRemove - 1:
            curr = curr.next
            i +=1
        curr.next = curr.next.next

        return head
