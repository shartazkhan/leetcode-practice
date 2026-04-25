class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        mylen = len(haystack) - len(needle) + 1

        for index in range(mylen):
            
            if haystack[index:len(needle)+index] == needle:
                return index
                
        return -1
