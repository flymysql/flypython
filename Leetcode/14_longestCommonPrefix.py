"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""

class Solution:
    def longestCommonPrefix(self, s) -> str:
        rel = ""
        for i in range(10000):
            try:
                tmp = s[0][i]
                flag = True
                for x in s[1:]:
                    if x[i] != tmp:
                        flag = False
                if flag == False:
                    return rel
                else:
                    rel += tmp
            except:
                return rel

"""
执行用时 : 52 ms, 在Longest Common Prefix的Python3提交中击败了83.96% 的用户
内存消耗 : 13.2 MB, 在Longest Common Prefix的Python3提交中击败了47.45% 的用户
"""
