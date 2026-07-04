class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, comb = [], []
        candidates.sort()

        def backtrack(ind, cur_sum):
            if cur_sum == target:
                res.append(comb[:])
                return

            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if cur_sum + candidates[i] > target:
                    break
                comb.append(candidates[i])
                backtrack(i + 1, cur_sum + candidates[i])
                comb.pop()
        
        backtrack(0, 0)
        return res