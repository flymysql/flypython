class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        tmp = 1
        tt = 1
        f = 0
        r = 0
        for i in range(1, len(s)):
            if s[i] in s[f:i]:
                if tmp > tt:
                    tt = tmp
                tmp -= s[f:i].index(s[i])
                f = f + s[f:i].index(s[i]) + 1
            else:
                tmp += 1
        if tmp > tt:
            tt = tmp  
        return tt

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
