# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [i for i in lists if i is not None]

        heap = []
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        curr = dummy
        while len(heap) > 0:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
            