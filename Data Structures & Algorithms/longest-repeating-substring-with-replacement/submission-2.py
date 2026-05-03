class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        right = 0
        hashMap = defaultdict(int)
        
        while right < len(s):
            hashMap[s[right]] += 1
            max_value = max(hashMap.values())
            if (right - left + 1) - max_value <= k:
                result = max(result, (right - left + 1))
            else:
                hashMap[s[left]] -= 1
                left += 1
            right +=1
        
        return result