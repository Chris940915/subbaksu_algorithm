

# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/

'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        n = len(nums)

        while fast < n:
            # 다를 경우, 
            if nums[fast] != nums[slow]:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
        return slow + 1
