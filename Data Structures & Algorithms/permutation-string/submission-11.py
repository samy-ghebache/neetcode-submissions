class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap = Counter(s1)
        for i in range(len(s2)):
            local = Counter(s2[i: i + len(s1)])
            if hashMap == local:
                return True
        return False
