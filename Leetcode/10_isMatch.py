"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
"""
class Solution:
    def __init__(self):
        self.arr = []
    def isMatch(self, s: str, p: str) -> bool:
        self.arr = [[-1 for i in range(len(p)+1)] for j in range(len(s)+1)]
        return self.match(s, p ,0 , 0)
    def match(self, s: str, p: str, i: int, j: int) -> bool:
        if self.arr[i][j] != -1:
            return self.arr[i][j]
        pp ,ss = p[j:], s[i:]
        lp, ls = len(pp), len(ss)
        if lp <= 0:
            return ls <= 0
        if ls <= 0:
            try:
                self.arr[i][j] = lp <= 0 or pp[1] == '*' and lp >= 2 and self.match(s, p, i , j+2)
                return self.arr[i][j]
            except:
                self.arr[i][j] = False
                return False
        match = (ls > 0 and ss[0] == pp[0]) or pp[0] == '.'
        if lp > 1 and pp[1] == '*':
            self.arr[i][j] = self.match(s, p, i, j+2) or (match and self.match(s, p, i+1, j))
            return self.arr[i][j]
        else:
            if match:
                self.arr[i][j] = self.match(s, p, i+1, j+1)
                return self.arr[i][j]
            self.arr[i][j] = False
            return False

"""
执行用时 : 76 ms, 在Regular Expression Matching的Python3提交中击败了93.59% 的用户
内存消耗 : 13.2 MB, 在Regular Expression Matching的Python3提交中击败了58.15% 的用户
"""