# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None:
            newhead = Node(insertVal)
            newhead.next = newhead
            return newhead

        curr = head
        while curr:
            if curr.val <= insertVal <= curr.next.val:
                newNode = Node(insertVal, curr.next)
                curr.next = newNode
                break
            elif curr.next.val < curr.val and (insertVal >= curr.val or insertVal <= curr.next.val):      
                newNode = Node(insertVal, curr.next)
                curr.next = newNode
                break
            elif curr.next == head:
                newNode = Node(insertVal, curr.next)
                curr.next = newNode
                break
            else:
                curr = curr.next
        return head