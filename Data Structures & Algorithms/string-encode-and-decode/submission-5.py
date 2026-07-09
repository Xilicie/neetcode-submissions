class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for w in strs:
            encoded.append(f"{len(w)}#{w}")

        return "".join(encoded)



    def decode(self, s: str) -> List[str]:

        def find_delim(s, i):
            while s[i] != "#":
                i += 1
            return i
        
        decoded = []


        i = 0 
        j = 0
        while i < len(s):
            i = find_delim(s, i)
            j = int(s[j:i])


            decoded.append(s[i+1:i+j+1])
            i += j + 1
            j = i
        
        return decoded

            




