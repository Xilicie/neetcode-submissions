class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}   # tuple : list

        for s in strs:

            arr = [0] * 26

            for i in range(len(s)):
                arr[ord(s[i]) - ord('a')] += 1
            
            if tuple(arr) in hash_map:
                hash_map[tuple(arr)].append(s)
            else:
                hash_map[tuple(arr)] = [s]

        res = []
        for value in hash_map.values():
            res.append(value)
        
        return res
        


        
