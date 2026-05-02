class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hashSet = set()
        result = 0
        for j in range(len(s)):
            while s[j] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[j])
            result = max(result, j - left + 1)
        return result