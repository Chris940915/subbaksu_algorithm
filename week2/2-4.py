

# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/


'''
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
'''

import heapq

class Solution:
    def thirdMax(self, nums) -> int:
        q = []
        result = 0

        for num in nums:
            if -num not in q:
                heapq.heappush(q, -num)

        if len(q) < 3:
            temp = [-num for num in q]
            return max(temp)

        for _ in range(3):
            result = heapq.heappop(q)
        return -result


numbers = [2, 2, 3, 1]
s = Solution()
print(s.thirdMax(numbers))