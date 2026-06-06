class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if not self.upper or num > self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)

        if len(self.upper) > len(self.lower) + 1:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
        elif len(self.lower) > len(self.upper):
            heapq.heappush(self.upper, -heapq.heappop(self.lower))

    def findMedian(self) -> float:
        if len(self.upper) > len(self.lower):
            return float(self.upper[0])
        return ((-self.lower[0]) + self.upper[0]) / 2.0