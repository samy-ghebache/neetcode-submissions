class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_result = 0
        for i in range(len(s)):
            j = i + 1
            local_set = set()
            local_set.add(s[i])
            while j < len(s) and s[j] not in local_set :
                local_set.add(s[j])
                j+= 1

            max_result = max(max_result, len(local_set))
        return max_result