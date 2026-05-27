# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        if head.next == head:
            newNode = Node(insertVal, head)
            head.next = newNode
            return head

        curr = head
        while True:
            # Case 1: insertVal is between two nodes (e.g., 1 -> [2] -> 3)
            if curr.val <= insertVal <= curr.next.val:
                break
            # Case 2: curr is the tail (max) and next is the head (min)
            elif curr.val > curr.next.val:
                # insertVal is the new max or the new min
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break
            curr = curr.next
            
            # Case 3: We looped back to the start without finding a pivot/gap
            # (e.g., all nodes have the same value)
            if curr == head:
                break
            
                
        later = curr.next
        newNode = Node(insertVal, later)
        curr.next = newNode

        return head