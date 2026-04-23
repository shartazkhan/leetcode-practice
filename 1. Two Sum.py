class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {} 

        for index, number in enumerate(nums):
            complement = target - number

            if complement in complement_map:
                return [complement_map[complement], index]
            complement_map[number] = index

        return[]
