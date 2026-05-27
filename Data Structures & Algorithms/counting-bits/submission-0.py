class Solution:
    def countBits(self, n: int) -> List[int]:
        numOnes = []
        for num in range(0, n+1):
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count +=1
                num = num >> 1
            numOnes.append(count)

        return numOnes