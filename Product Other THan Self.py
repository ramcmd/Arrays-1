# TC: O(n) where n is the len of the array
# SC: O(1) because we are not creating an additional auxillary DS to store any nums other 
# than the result itself

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Running product
        
        result = [1] * len(nums)
        
        rp = 1
        
        for i in range(1, len(nums)):
            rp*= nums[i-1]
            result[i] = rp
        
        rp = 1
        
        for i in range(len(nums)-2, -1, -1):
            rp*= nums[i+1]
            result[i] *= rp
        
        return result
            
        
        