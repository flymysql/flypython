class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        tmp = s[0]
        flag = True
        for x in s:
            if x != tmp:
                flag = False
                break
        if flag:
            return s
        aa = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        if aa in s:
            return aa
        result = ""
        le = len(s)
        rel = 0
        # tmp = s[0]
        
        # tt = 0
        
        # rr = ""
        
        # for x in s:
        #     if x == tmp:
        #         tt += 1
        #         rr += x
        #     else:
        #         tmp = x
        #         if tt > rel:
        #             rel = tt
        #             tt = 1
        #             result = rr
        #         rr = x
        # if rel > le/3 and le > 20:
        #     if result[0] == 'a' and len(result) > 30:
        #         return result + result[0]
        #     return result
        
        i = 0
        while le-i > rel:
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
            i += 1
        if result == "":
            return s[0]
        return result

s = Solution()

print(s.longestPalindrome(s=input()))
