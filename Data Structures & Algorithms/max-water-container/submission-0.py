class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            right = len(heights) - 1
            while right > i:
                height = heights[i]
                if heights[right] < heights[i]:
                    height = heights[right]
                maxArea = max(maxArea, (right - i)*height)
                right -= 1

        return maxArea

        