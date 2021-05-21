'''
https://leetcode.com/contest/weekly-contest-239/problems/minimum-distance-to-the-target-element/


'''

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        a = []
        for i in range(len(nums)):
            if nums[i] == target:
                a.append(abs(i-start))
        return min(a)
        