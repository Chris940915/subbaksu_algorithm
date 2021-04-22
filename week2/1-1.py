

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.


# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"

# Input: s = "What is the solution to this problem", k = 4
# Output: "What is the solution"

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splitted_s = s.split(" ")
        result = ""
        if len(splitted_s) <= k:
            result = " ".join(splitted_s)
        else:
            splitted_s = splitted_s[:k]
            result = " ".join(splitted_s)
        return result

    def truncateSentence_2(self, s: str, k : int) -> str:
        for i, c in enumerate(s):
            if c == " ":
                k -= 1
                if k == 0:
                    return s[:i]

s = Solution()
print(s.truncateSentence("Hello how are you Contestant", 4))
