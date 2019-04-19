'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution:
    def twoSum(self, nums, target: int):
        lens = len(nums)
        for i in range(lens):
            if target-nums[i] in nums[i+1:]:
                return [i,nums[i+1:].index(target-nums[i])+i+1]
    def twoSum2(self, nums, target: int):
        maps = {}
        for i in nums:
            maps[i] = 1
        for j in nums:
            if target-j in maps:
                f = nums.index(j)
                if target-j in nums[f+1:]:
                    l = nums[f+1:].index(target-j) + f + 1
                    return [f, l]
        
    
s = Solution()
nums = [3,2,4]
target = 6
re = s.twoSum2(nums, target)
print(re)