'''
https://leetcode.com/contest/weekly-contest-238/problems/sum-of-digits-in-base-k/
'''

class Solution:

    def sumBase(self, n: int, k: int) -> int:
        def convert(num, base):
            NUMBER = "0123456789"
            q, r = divmod(num, base)

            if q == 0:
                return NUMBER[r]
            else:
                return convert(q, base) + NUMBER[r]

        tmp = convert(n, k)
        str_result = str(tmp)
        result = 0
        for t in tmp:
            result += int(t)
        return result
