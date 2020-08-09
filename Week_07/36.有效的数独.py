#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
# https://leetcode-cn.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (59.82%)
# Likes:    388
# Dislikes: 0
# Total Accepted:    87.5K
# Total Submissions: 144.9K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 
# 
# 上图是一个部分填充的有效的数独。
# 
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠ ["5","3",".",".","7",".",".",".","."],
# ⁠ ["6",".",".","1","9","5",".",".","."],
# ⁠ [".","9","8",".",".",".",".","6","."],
# ⁠ ["8",".",".",".","6",".",".",".","3"],
# ⁠ ["4",".",".","8",".","3",".",".","1"],
# ⁠ ["7",".",".",".","2",".",".",".","6"],
# ⁠ [".","6",".",".",".",".","2","8","."],
# ⁠ [".",".",".","4","1","9",".",".","5"],
# ⁠ [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# [
# ["8","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
# ⁠    但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
# 
# 说明:
# 
# 
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 给定数独序列只包含数字 1-9 和字符 '.' 。
# 给定数独永远是 9x9 形式的。
# 
# 
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lows, columns, boxes = defaultdict(set), defaultdict(set), defaultdict(set)        
        for low in range(9):
            for col in range(9): 
                if board[low][col].isdigit(): # 或者用 board[low][col] != '.'也可以
                    # #以下三个if判断是不是在行、列和 3*3宫格内存在有重复数字
                    if board[low][col] in lows[low]:
                        return False
                    if board[low][col] in columns[col]:
                        return False
                    #这里3*3宫格缩小1/3
                    if board[low][col] in boxes[low // 3, col // 3]:
                        return False
                    #没存在加入行、列和 3*3宫格
                    lows[low].add(board[low][col])
                    columns[col].add(board[low][col])
                    boxes[low // 3, col // 3].add(board[low][col])
                    
        return True
# @lc code=end

