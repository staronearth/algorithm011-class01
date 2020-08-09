#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (75.58%)
# Likes:    1146
# Dislikes: 0
# Total Accepted:    145.3K
# Total Submissions: 191.9K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #DFS实现
        res = []
        s = ""
        def helper(left:int,right:int,n,s):
            #recursion terminator 
            if left == n and right == n:
                return res.append(s)
            #current logic
            if left < n:
                #drill down
                helper(left+1,right,n,s+'(')
            if left > right:
                helper(left,right+1,n,s+')')
        helper(0,0,n,s)
        return res
        #BFS
        # import queue
        # que = queue.Queue()
        # def BFS()
# @lc code=end

