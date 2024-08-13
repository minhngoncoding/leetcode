class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dct = {}

        for index, num in enumerate(nums):

            if num not in sum_dct.keys():
                sum_dct[target-num] = index
            else:
                return [index, sum_dct[num]]

        

                

            
