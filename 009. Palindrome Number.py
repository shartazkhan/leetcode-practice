class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_x = str(x)
        reverse_x = str_x[::-1]

        if str_x == reverse_x:
            return True
        else:
            return False
