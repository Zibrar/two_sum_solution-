class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)) : #outerloop
          for j in range((i + 1) , len(nums)): # inner loop 
              if nums[i] + nums[j] == target  : #condition for said loop 
               return (i,j) 
               return []  
            


        

        