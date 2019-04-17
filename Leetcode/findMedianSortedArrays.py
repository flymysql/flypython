class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        num = nums1 + nums2
        num.sort()
        le = len(num)
        if le % 2 == 0:
            return float((num[int(le/2)-1] + num[int(le/2)]) / 2)
        else:
            return float(num[int(le/2)])
        # if (len1 + len2) % 2 == 0:
        #     l1 = 0
        #     l2 = 0
        #     for i in range((len1 + len2) / 2):
        #         if nums1[l1] > nums1[]

s = Solution()
print(s.findMedianSortedArrays([4,5,6],[2,3]))