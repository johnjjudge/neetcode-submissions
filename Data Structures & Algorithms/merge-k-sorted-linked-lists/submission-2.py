# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Remove empty lists initially
        #lists = [l for l in lists if l is not None]

        dummy = ListNode()
        curr = dummy
        min_heap = []
        # Add first node of each list into a heap
        for i, node in enumerate(lists):
            heapq.heappush(min_heap, (node.val, i))
        
        while len(min_heap) > 0:
            val, i = heapq.heappop(min_heap)
            curr.next = lists[i]
            curr = curr.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(min_heap, (lists[i].val, i))
        
        return dummy.next
