class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        for l in range(len(heights)-1):
            r = l +1
            while r < len(heights):
                maxWater = max(maxWater, min(heights[l], heights[r])*(abs(r-l)))
                r += 1
        return maxWater