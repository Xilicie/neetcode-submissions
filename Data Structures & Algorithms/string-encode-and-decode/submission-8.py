class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for w in strs:
            encoded.append(f"{len(w)}#{w}")

        return "".join(encoded)



    def decode(self, s: str) -> List[str]:
        
        decoded = []


        delim = 0 
        start = 0
        length = 0
        while start < len(s):
            delim = s.find('#', start)
            length = int(s[start:delim])

            decoded.append(s[delim+1:delim+length+1])
            start = delim + length + 1
        
        return decoded

            




