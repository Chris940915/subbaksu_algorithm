class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        sum_v = nums[0]
        max_v = sum_v

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                sum_v += nums[i]
            else:
                sum_v = nums[i]
            max_v = max(max_v, sum_v)
        return max_v