class Solution:
    def hammingWeight(self, n: int) -> int:
        nb = str(bin(n))
        ones = 0
        for i in range(len(nb)):
            if nb[i] == "1":
                ones +=1
        return ones
