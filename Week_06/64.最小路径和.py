#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (65.73%)
# Likes:    596
# Dislikes: 0
# Total Accepted:    128K
# Total Submissions: 190K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # res = 0
        # 递归求解
        
        # dp求解
        m = len(grid)
        n = len(grid[0])
        for i in range(1,m):
            grid[i][0] = grid[i][0]+grid[i-1][0]
        for j in range(1,n):
            grid[0][j] = grid[0][j]+grid[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                # print(grid[i][j])
                grid[i][j]=min(grid[i][j]+grid[i][j-1],grid[i][j]+grid[i-1][j])
        return grid[-1][-1]
# @lc code=end

