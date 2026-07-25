class Solution:
    def grayCode(self, n: int) -> List[int]:
        #Solution 2
        #THE Math trick - gray_code(i)=i xor (i>>1)
        ans = []
        for i in range(2**n):
            ans.append(i^(i>>1))
        return ans