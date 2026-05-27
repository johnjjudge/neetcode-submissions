class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        freqs = []
        for kv in counts:
            freqs.append((counts[kv], kv))
        freqs.sort()
        result = []
        for i in range(len(freqs)-1, len(freqs) - k-1,-1):
            result.append(freqs[i][1])
        return result

