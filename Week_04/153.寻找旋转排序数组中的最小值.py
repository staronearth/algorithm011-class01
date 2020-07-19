#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (50.96%)
# Likes:    214
# Dislikes: 0
# Total Accepted:    61.3K
# Total Submissions: 119.8K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
# 
# 请找出其中最小的元素。
# 
# 你可以假设数组中不存在重复元素。
# 
# 示例 1:
# 
# 输入: [3,4,5,1,2]
# 输出: 1
# 
# 示例 2:
# 
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        while (left < right):
            mid=int((left+right)/2)
            if nums[mid]>nums[right]:
                # 代表右边无序，将右边界移到mid右边
                left = mid + 1
            else:
                # 代表左边无序，将左边界移到mid处
                right = mid 
        return nums[left]
# @lc code=end

