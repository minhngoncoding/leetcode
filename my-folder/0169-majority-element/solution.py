class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num not in hash_table.keys():
                hash_table[num] = 1
            else:
                hash_table[num] += 1
                if hash_table[num] > len(nums)//2:
                    return num
