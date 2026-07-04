class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        working_on = set()
        output = []

        l = 0
        for r in range(len(s)):
            working_on.add(s[r])
            count[s[r]] -= 1

            if not count[s[r]]:
                working_on.discard(s[r])

            if not working_on:
                output.append(r - l + 1)
                l = r + 1
        return output


            