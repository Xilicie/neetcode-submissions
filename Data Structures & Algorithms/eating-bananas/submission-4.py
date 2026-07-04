class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper bound for k
        left, right = 1, max(piles)
        k = right
        while left <= right:
            middle = left + (right - left) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middle)

            if hours > h:
                left = middle + 1
            elif hours <= h:
                k = middle
                right = middle - 1
        return k
            
