# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal, head)
            return head
        
        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                curr.next = Node(insertVal, curr.next)
                return head
            elif curr.val > curr.next.val and (insertVal >= curr.val or insertVal <= curr.next.val):
                curr.next = Node(insertVal, curr.next)
                return head
            elif curr.next == head:
                curr.next = Node(insertVal, curr.next)
                return head
            curr = curr.next

        return head
        