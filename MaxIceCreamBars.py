class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        
        for x in costs:
            if(coins-x >= 0):
                count = count + 1
                coins = coins - x
        
        return count
