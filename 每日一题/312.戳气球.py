#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#


# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(total, rec[i][j])
        return rec[0][n+1]

# @lc code=end
