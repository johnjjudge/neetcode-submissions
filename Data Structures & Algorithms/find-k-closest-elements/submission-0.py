class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.findClosest(arr, x)
        l = index
        r = index + 1
        result = collections.deque([])
        while len(result) < k:
            if l < 0:
                result.append(arr[r])
                r+=1
            elif r == len(arr):
                result.appendleft(arr[l])
                l-=1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                result.appendleft(arr[l])
                l-=1
            else:
                result.append(arr[r])
                r+=1
        return list(result)


    def findClosest(self, arr, target):
        lo = 0
        hi = len(arr) - 1
        best_idx = 0

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if abs(arr[mid] - target) < abs(arr[best_idx] - target):
                best_idx = mid
            elif abs(arr[mid] - target) == abs(arr[best_idx] - target):
                if arr[mid] < arr[best_idx]:
                    best_idx = mid

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return best_idx