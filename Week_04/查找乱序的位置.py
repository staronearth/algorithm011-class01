class Solution:
    def search(self, nums) -> int:
        left,right = 0,len(nums)-1
        while (left <right):
            mid=int((left+right)/2)
            print(nums[mid])
            if nums[mid]>nums[right]:
                # 代表左边有序，将右边界移到mid右边
                left = mid + 1
            else:
                # 代表右边有序，将左边界移到mid的左边
                right = mid 
        return left

nums=[2,3,4,5,1]

re = Solution().search(nums)

print(nums[re])