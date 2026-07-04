class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        seen, res, comb = set(), [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, cur_sum):
            if cur_sum == target and tuple(comb) not in seen:
                seen.add(tuple(comb))
                res.append(comb[:])
                return
            if i == n or cur_sum > target:
                return
            comb.append(candidates[i])
            backtrack(i+1, cur_sum + candidates[i])
            comb.pop()

            backtrack(i+1, cur_sum)

        backtrack(0, 0)
        return res

        