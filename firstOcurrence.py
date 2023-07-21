#First solution

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1

# Second Solution
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
