class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for num in nums:
            local_result = 1
            if num - 1 not in nums_set:
                # the first element
                while num + local_result in nums_set:
                    local_result += 1
            result = max(result, local_result)
        return result
        
