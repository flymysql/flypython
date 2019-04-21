"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        s = nums[0] + nums[-1] + nums[-2]
        rel = abs(s - target)
        for i in range(len(nums)-1):
            if nums[i-1] < nums[i] or i == 0:
                mid = i + 1
                r = len(nums) - 1
                while mid < r:
                    tsum = nums[i] + nums[mid] + nums[r]
                    t = abs(tsum - target)
                    if t < rel:
                        rel = t
                        s = tsum
                    if tsum > target:
                        r -= 1
                        while mid < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif tsum < target:
                        mid += 1
                        while mid < r and nums[mid] == nums[mid-1]:
                            mid += 1
                    elif tsum == target:
                        return tsum
        return s

"""
执行用时 : 108 ms, 在3Sum Closest的Python3提交中击败了94.45% 的用户
内存消耗 : 13.1 MB, 在3Sum Closest的Python3提交中击败了76.47% 的用户
"""


