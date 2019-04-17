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