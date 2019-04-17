class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        result = ""
        rel = 0
        le = len(s)
        for i in range(le):
            j = le -1
            while j > i:
                jj = j
                ii = i
                while ii < jj:
                    if s[ii] == s[jj]:
                        ii += 1
                        jj -= 1
                    else:
                        break
                if ii >= jj:
                    if j+1-i > rel:
                        result = s[i:j+1]
                        rel = len(result)
                        break
                j -= 1
        if result == "":
            return s[0]
        return result

s = Solution()

print(s.longestPalindrome(s=input()))
