class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1+1:]):
                if num2 == (target - num1):
                    return [index1, index1+index2+1]
            

                  
