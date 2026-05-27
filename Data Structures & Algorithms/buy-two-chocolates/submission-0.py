class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest = [min(prices[0], prices[1]), max(prices[0], prices[1])]
        i = 2
        while i < len(prices):
            price = prices[i]
            if price >= smallest[1]:
                i+=1
                continue
            elif price >= smallest[0] and price < smallest[1]:
                smallest[1] = price
            elif price < smallest[0]:
                smallest[1] = smallest[0]
                smallest[0] = price
            i+=1
        leftover = money - smallest[1] - smallest[0]
        if leftover < 0:
            return money
        return leftover