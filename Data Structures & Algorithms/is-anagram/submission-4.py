class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_a, t_a = Counter(s), Counter(t)
        return s_a == t_a