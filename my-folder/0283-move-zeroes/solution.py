class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        left = 0
        right = 1

        for i in range(0, len(nums)-1):
            if nums[left] == 0:
                if nums[right] != 0:
                    nums[left] = nums[right]
                    nums[right] = 0
                    left += 1
            else:
                left += 1
            right += 1

        return nums
                




        
