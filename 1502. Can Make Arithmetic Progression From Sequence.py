class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        temp = 0
        curr = 0

        arr.sort()
        for i in range(len(arr)):
            if i == 0:
                curr = arr[i+1] - arr[i]
            if i == len(arr)-1:
                return True
                
            temp = arr[i+1] - arr[i]
            
            if curr == temp:
                curr = temp
            else:
                return False
