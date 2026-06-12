# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        nodesLower = deque(nodes[:len(nodes)//2])
        nodesUpper = deque(nodes[len(nodes)//2:][::-1])

        dummy = ListNode()
        curr = dummy
        while len(nodesLower) > 0 or len(nodesUpper) > 0:
            lowerNode = None
            upperNode = None
            if len(nodesLower) > 0:
                lowerNode = nodesLower.popleft()
            if len(nodesUpper) > 0:
                upperNode = nodesUpper.popleft()
            if lowerNode:
                curr.next = lowerNode
                curr = curr.next
            if upperNode:
                curr.next = upperNode
                curr = curr.next
        curr.next = None
