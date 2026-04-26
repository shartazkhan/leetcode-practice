class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums_copy = nums.copy()
        nums_copy.sort()

        if nums_copy == nums:
            return True
            
        nums_copy.sort(reverse=True)

        if nums_copy == nums:
            return True


        return False
                
