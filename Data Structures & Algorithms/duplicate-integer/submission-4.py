class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seek = set()

        for val in nums:
            if val in seek:
                return True
            else:
                seek.add(val)
        return False