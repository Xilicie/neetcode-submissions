class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_seq = 1
        elements = set(nums)

        for num in elements:
            if num - 1 in elements:
                continue

            cur_seq = 1
            while num + 1 in elements:
                num += 1
                cur_seq += 1
        
            max_seq = max(max_seq, cur_seq)
        
        return max_seq
                
            