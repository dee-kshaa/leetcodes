class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            l.append(i)
        for i in nums:
            l.append(i)
        return l

