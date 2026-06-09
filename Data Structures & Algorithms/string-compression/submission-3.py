class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)
        l = 0
        r = l+1
        i = 0
        while l < len(chars):
            r = l + 1
            while r < len(chars) and chars[r] == chars[l]:
                r+=1
            chars[i] = chars[l]
            i+=1    
            if r > l+1:
                num = str(r - l)
                for n in range(len(num)):
                    chars[i+n] = num[n]
                i += len(num)
            l = r
        return i