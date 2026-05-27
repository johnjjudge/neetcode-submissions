class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        atrustsb = {}
        bistrustedbya = {}
        for t in trust:
            if t[0] not in atrustsb:
                atrustsb[t[0]] = set([t[1]])
            else:
                atrustsb[t[0]].add(t[1])
            if t[1] not in bistrustedbya:
                bistrustedbya[t[1]] = set([t[0]])
            else:
                bistrustedbya[t[1]].add(t[0])
        for i in range(1, n + 1):
            if i not in atrustsb and bistrustedbya.get(i) and len(bistrustedbya[i]) == n-1:
                return i
        return -1
