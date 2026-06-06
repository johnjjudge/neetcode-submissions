# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # find the smallest node in list
        # find second smallest node in list
        # if second smallest < smallest.next, then smallest.next = secondSmallest, secondSmallest = smallest and smallest = smallest.next, if either are null then remove from list
        # continue until list size == 1
        # since we always are only concerned with the two smallest elements a heap is a good choice
        if len(lists) == 0:
            return None
        heaplist = []
        for i, node in enumerate(lists):
            if node != None:
                heaplist.append((node.val, i, node))
        heapq.heapify(heaplist)
        if not heaplist:
            return None
        
        dummy = ListNode(0)
        current = dummy
        
        while heaplist:
            val, i, node = heapq.heappop(heaplist)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heaplist, (node.next.val, i, node.next))
        
        return dummy.next