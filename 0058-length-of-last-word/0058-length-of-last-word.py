class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        """
        l=s.split()
        for i in l:
            s1=len(l[-1])
        return s1