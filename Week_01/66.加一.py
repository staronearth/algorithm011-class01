#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (44.39%)
# Likes:    487
# Dislikes: 0
# Total Accepted:    166.3K
# Total Submissions: 374.4K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#
#我的想法是
# 1.先将数组反向输出
# 2.给输出的从最后一位开始加1
# 3.如果大于十就对下一个位数进行加1，并将这个位数置为0
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        zero_list=[0]
        digits=zero_list+digits
        for i in range(1,len(digits)+1):
            if digits[-i]+1>=10:
                digits[-i]=0
                digits[-i-1]=digits[-i-1]+1
            else:
                digits[-i]=digits[-i]+1
                break          
        if digits[0]==0:
            digits=digits[1:len(digits)]
        return digits

# @lc code=end

