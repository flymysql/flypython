"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution:
    def letterCombinations(self, digits: str):
        dics = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        rel = []
        r = len(digits) - 1
        while r >= 0:
            cur = dics[int(digits[r])]
            if cur != "":
                if rel != []:
                    tmp = []
                    for x in cur:
                        for t in rel:
                            tmp.append(x+t)
                    rel = tmp
                else:
                    for x in cur:
                        rel.append(x)
            r -= 1
        return rel
"""
执行用时 : 52 ms, 在Letter Combinations of a Phone Number的Python3提交中击败了83.69% 的用户
内存消耗 : 13.1 MB, 在Letter Combinations of a Phone Number的Python3提交中击败了59.74% 的用户
"""