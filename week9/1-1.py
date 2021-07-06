'''
https://leetcode.com/contest/weekly-contest-245/problems/redistribute-characters-to-make-all-strings-equal/
'''

class Solution:
    def makeEqual(self, words) -> bool:
        entire_words = ""
        for word in words:
            entire_words += word

        unique_chars = set(entire_words)
        n_words = len(words)

        for unique_char in unique_chars:
            if entire_words.count(unique_char) % n_words != 0:
                return False
        return True