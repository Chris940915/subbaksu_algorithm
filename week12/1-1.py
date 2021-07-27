'''

https://leetcode.com/contest/weekly-contest-247/problems/maximum-product-difference-between-two-pairs/

'''

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_nums = nums.sort()
        max_v = nums[-1] * nums[-2]
        min_v = nums[0] * nums[1]

        return max_v-min_v