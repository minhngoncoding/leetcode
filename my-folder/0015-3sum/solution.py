class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_dct = {}

        nums.sort()
        result = []
        temp = -inf
        for i in range(len(nums)-1):
            # This case already handle if previous loop
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            if nums[i] > 0:
                break

            while j < k:
                if nums[k] < 0:
                    break

                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                   

        return result
