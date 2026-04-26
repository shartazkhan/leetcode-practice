class Solution:
    def arraySign(self, nums: List[int]) -> int:
        b = 1

        for i in nums:
            b = b * i
            
        if b > 0:
            return 1
        if b < 0:
            return -1
        else:
            return 0
