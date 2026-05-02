class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp_string = (s+s)[1:-1]
        return s in temp_string
