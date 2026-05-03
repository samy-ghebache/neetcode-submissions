class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Set = Counter(s1)
        for i in range(len(s2)):
            if s2[i] in s1Set:
                j = i + 1
                counter = 1
                hashMap = defaultdict(int)
                hashMap[s2[i]] = 1
                while j < len(s2) and (s2[j] in s1Set) and hashMap[s2[j]] < s1Set[s2[j]]:
                    counter +=1
                    hashMap[s2[j]] +=1
                    j+=1
                if counter == len(s1):
                    return True
        return False
