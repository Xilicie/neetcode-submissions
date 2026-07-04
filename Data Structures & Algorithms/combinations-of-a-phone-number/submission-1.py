class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }
        res, combo = [], []
        def bt(i):
            if i == len(digits):
                res.append(''.join(combo))
                return
            for letter in keys[digits[i]]:
                combo.append(letter)
                bt(i + 1)
                combo.pop()
        if not digits:
            return res
        bt(0)
        return res

