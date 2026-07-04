class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        frequencies = Counter(hand)
        hand.sort()

        for num in hand:
            if frequencies[num]:
                for i in range(num, num + groupSize):
                    if not frequencies[i]:
                        return False
                    frequencies[i] -= 1
        return True


        

        