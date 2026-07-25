class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        temp = max(nums)
        logn = int(math.log2(temp))
        mx = 2**(logn+1)
        singlet = set()
        doublet = {0}
        triplet = set()

        while nums:
            v = nums.pop()
            if v in singlet:
                continue
            singlet.add(v)
            for u in singlet:
                doublet.add(u^v)
            
            for u in doublet:
                triplet.add(u^v)
            if len(triplet) == mx:
                return mx

        return len(triplet)