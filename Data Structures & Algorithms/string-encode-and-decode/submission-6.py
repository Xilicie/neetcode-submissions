class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for w in strs:
            encoded.append(f"{len(w)}#{w}")

        return "".join(encoded)



    def decode(self, s: str) -> List[str]:
        
        decoded = []


        i = 0 
        j = 0
        length = 0
        while i < len(s):
            i = s.find('#', i)
            length = int(s[j:i])


            decoded.append(s[i+1:i+length+1])
            i += length + 1
            j = i
        
        return decoded

            




