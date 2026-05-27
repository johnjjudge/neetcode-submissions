class MedianFinder:

    def __init__(self):
        self.minHeap = [] # upper numbers
        self.maxHeap = [] # lower numbers, need to put in as negative

    def addNum(self, num: int) -> None:
        if self.minHeap == [] or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        else:
            return float(self.minHeap[0] + (-1 * self.maxHeap[0])) / 2.0
        
        