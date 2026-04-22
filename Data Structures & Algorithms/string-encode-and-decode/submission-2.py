class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for s in strs:
            new_string = new_string + str(len(s)) + "#" + s
        return new_string
    def decode(self, s: str) -> List[str]:
        idx = 0
        result = []
        while idx < len(s):
            str_len = 0
            while idx < len(s) and s[idx].isdigit()  and s[idx]!="#":
                str_len  = str_len*10 + int(s[idx])
                idx+=1
            if idx == len(s):
                break
            if s[idx] == "#":
                idx+=1
            result.append(s[idx:idx+str_len])
            idx = idx + str_len
        return result

            
        