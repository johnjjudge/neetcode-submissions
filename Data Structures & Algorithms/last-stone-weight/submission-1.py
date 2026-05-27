class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            two_biggest = [heapq.heappop_max(stones), heapq.heappop_max(stones)]
            if two_biggest[0] != two_biggest[1]:
                heapq.heappush_max(stones, two_biggest[0]-two_biggest[1])
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
                
        