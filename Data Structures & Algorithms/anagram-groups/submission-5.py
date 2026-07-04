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
        
        return list(hash_map.values())
        


        
