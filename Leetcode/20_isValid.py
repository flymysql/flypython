"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        lcp, rcp = ['{', '(', '['], ['}', ')', ']']
        tmp = []
        le = len(s)
        for i in range(le):
            if s[i] in lcp:
                tmp.append(s[i])
            elif not tmp or rcp[lcp.index(tmp.pop())] != s[i]:
                return False
        if tmp:
            return False
        return True
"""
执行用时 : 52 ms, 在Valid Parentheses的Python3提交中击败了83.83% 的用户
内存消耗 : 13.1 MB, 在Valid Parentheses的Python3提交中击败了84.43% 的用户
"""

        