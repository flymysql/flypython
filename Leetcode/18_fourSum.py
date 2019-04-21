"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d 
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

示例：给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res =[]
        i = 0
        for f in range(len(nums)-3):
            if nums[f] > target and target > 0:
                break
            if f == 0 or nums[f-1] < nums[f]:
                for i in range(f+1, len(nums)):
                    if nums[i] + nums[f] > target and target > 0:
                        break
                    if i == f+1 or nums[i-1] < nums[i]:
                        l = i+1
                        r = len(nums) - 1
                        while l < r:
                            s = nums[i] + nums[l] + nums[r] + nums[f]
                            if s == target:
                                res.append([nums[f], nums[i], nums[l], nums[r]])
                                l += 1
                                r -= 1
                                while l < r and nums[l] == nums[l-1]:
                                    l += 1
                                while r > l and nums[r] == nums[r+1]:
                                    r -= 1
                            elif s > target:
                                r -= 1
                            else :
                                l += 1
        return res

"""
执行用时 : 1244 ms, 在4Sum的Python3提交中击败了47.59% 的用户
内存消耗 : 13.2 MB, 在4Sum的Python3提交中击败了48.10% 的用户
"""
