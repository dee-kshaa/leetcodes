class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        h = [[-v,k] for k,v in counter.items()]

        heapq.heapify(h)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(h)[1])

        return res