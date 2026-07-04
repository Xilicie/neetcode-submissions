class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [0, 0, 0]

        for trp in triplets:
            if trp == target:
                return True
        
            fits = True
            for i in range(3):
                if trp[i] > target[i]:
                    fits = False
                    break
            
            if fits:
                for i in range(3):
                    found[i] = max(found[i], trp[i])
        
        return found == target