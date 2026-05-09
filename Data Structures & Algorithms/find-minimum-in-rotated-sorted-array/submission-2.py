class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = float('inf')

        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # problem
                result = min(result, nums[mid])
                right = mid
            else:
                left = mid + 1
        return result




