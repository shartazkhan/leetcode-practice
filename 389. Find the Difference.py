class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        the_word = ""
        t = ''.join(sorted(t))
        s = ''.join(sorted(s))

        for inedx in range(len(s)):
            if s[inedx] != t[inedx]:
                the_word = t[inedx]
                break


        if the_word.strip() == "":
            return t[len(s):]
        else:
            return the_word  
