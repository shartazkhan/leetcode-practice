class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.split(" ")
        t = list(filter(lambda x: x, t))

        return len(t[-1])
