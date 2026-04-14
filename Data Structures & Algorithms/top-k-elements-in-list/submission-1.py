class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seek = {}

        for num in nums:
            seek[num] = seek.get(num, 0) + 1
        
        print(seek)
        arr = []
        for num,cnt in seek.items():
            arr.append([cnt,num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res