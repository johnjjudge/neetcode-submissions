class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for i in counts:
            if counts[i] > len(nums)/2:
                return i
        