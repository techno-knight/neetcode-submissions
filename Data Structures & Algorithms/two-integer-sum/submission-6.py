class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seek = {}

        for i,val in enumerate(nums):
            diff = target - val

            if diff in seek:
                return [seek[diff],i]
            
            seek[val] = i