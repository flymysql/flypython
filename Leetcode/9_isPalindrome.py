'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

"""
执行用时 : 104 ms, 在Palindrome Number的Python3提交中击败了99.58% 的用户
内存消耗 : 13.2 MB, 在Palindrome Number的Python3提交中击败了82.83% 的用户
"""