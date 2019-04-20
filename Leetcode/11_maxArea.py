"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
"""
class Solution:
    def maxArea(self, height) -> int:
        h = 0
        maxa = 0
        le = len(height)
        hh = height[::-1]
        for i in range(le):
            if height[i] > h:
                for j in range(le - i):
                    if hh[j] >= height[i]:
                        if (le - j - i - 1) * height[i] > maxa:
                            maxa = (le - j - i - 1) * height[i]
                        break
                    elif (le - j - i -1) * hh[j] > maxa:
                        maxa = (le - j - i - 1) * hh[j]
                h = height[i]
        return maxa

"""
执行用时 : 80 ms, 在Container With Most Water的Python3提交中击败了80.05% 的用户
内存消耗 : 14.4 MB, 在Container With Most Water的Python3提交中击败了65.81% 的用户
"""
                    
