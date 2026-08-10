class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked = 0
        
        for i in range(len(fruits)):
            baskets = set()
            pick = 0
            r = i
            while r < len(fruits):
                if len(baskets) == 2 and fruits[r] not in baskets:
                    break
                if len(baskets) < 2 or fruits[r] in baskets:
                    pick += 1
                    baskets.add(fruits[r])
                r+=1
            picked = max(picked,pick)
            
        return picked