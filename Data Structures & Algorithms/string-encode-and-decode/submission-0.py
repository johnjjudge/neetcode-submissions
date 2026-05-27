class Solution:



    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for i in range(len(strs)):
            encodedStr += "///" + strs[i]
        return encodedStr

    def decode(self, s: str) -> List[str]:
        return s.split("///")[1:]
