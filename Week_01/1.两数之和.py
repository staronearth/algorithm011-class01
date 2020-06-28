#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=0
        length=len(nums)
        blist=[]
        for i in range(length-1):
            for j in range(i+1,length):
                sum=nums[j]+nums[i]
                if(target==sum):
                    blist.append(i)
                    blist.append(j)
        return blist
        
# @lc code=end

