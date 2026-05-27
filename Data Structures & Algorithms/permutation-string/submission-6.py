class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_counts = Counter(s1)
        for i in range(n2 - n1 + 1):
            window_counts = Counter(s2[i:i+n1])
            if s1_counts == window_counts:
                return True
        return False