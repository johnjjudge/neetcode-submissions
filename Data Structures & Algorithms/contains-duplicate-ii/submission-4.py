class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vals = {}
        for i in range(len(nums)):
            if nums[i] not in vals:
                vals[nums[i]] = [i]
            else:
                for n in vals[nums[i]]:
                    if abs(n - i) <= k:
                        return True
                vals[nums[i]].append(i)
        return False