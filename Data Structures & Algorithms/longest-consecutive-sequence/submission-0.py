class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        i = 0
        result = 0

        while i < len(nums):
            previous = nums[i]
            i+=1
            new_seq = 1
            while i < len(nums) and nums[i] - previous == 1:
                new_seq +=1
                previous = nums[i]
                i+=1
            result = max(result, new_seq)
        return result
        
