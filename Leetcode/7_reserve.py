'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
'''
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        flag = ""
        if s[0] == '-':
            flag = s[0]
            s = s[1:]
        ls = int(flag + s[::-1])
        if ls < -2147483648 or ls >2147483647:
            ls = 0
        return ls

s = Solution()
print(s.reverse(-123))

'''
执行用时 : 56 ms, 在Reverse Integer的Python3提交中击败了98.64% 的用户
内存消耗 : 13.3 MB, 在Reverse Integer的Python3提交中击败了48.60% 的用户
'''