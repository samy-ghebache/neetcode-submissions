class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1HashMap = Counter(s1)
        s2HashMap = Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if s2HashMap == s1HashMap:
                return True
            s2HashMap[s2[i]] += 1
            s2HashMap[s2[i - len(s1)]] -= 1
            if s2HashMap[s2[i - len(s1)]] == 0:
                del s2HashMap[s2[i - len(s1)]]

        if s2HashMap == s1HashMap:
            return True

        return False
