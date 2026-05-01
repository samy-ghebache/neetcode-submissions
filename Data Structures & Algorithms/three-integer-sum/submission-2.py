class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 
        results = []
        i = 0
        while i < len(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                    temp_res = nums[i] + nums[left] + nums[right]
                    if temp_res == 0:
                        results.append([nums[i], nums[left], nums[right]])
                        left+=1
                        right-=1
                        while left < len(nums) and nums[left] == nums[left - 1]:
                            left+=1
                        while right > 0 and nums[right] == nums[right+1]:
                            right-=1
                    elif temp_res < 0:
                        left += 1
                    else:
                        right -=1
            i+= 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i+=1
                
        return results