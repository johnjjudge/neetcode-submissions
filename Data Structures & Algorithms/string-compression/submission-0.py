class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        p = 0
        while l < len(chars):
            r = l
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
            
            chars[p] = chars[l]
            p += 1
            
            count = r - l
            if count > 1:
                for digit in str(count):
                    chars[p] = digit
                    p += 1
            l = r
        return p