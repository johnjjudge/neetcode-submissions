class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                start = i
                n = 0
                while n < len(needle) and i < len(haystack) and needle[n] == haystack[i]:
                    n +=1
                    i +=1
                if n == len(needle):
                    return start
                i = start
            i+=1
        return -1
        