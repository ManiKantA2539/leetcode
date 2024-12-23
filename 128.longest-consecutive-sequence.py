#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        temp=0
        for i in range(0,len(nums)-1):
            if nums[i]+1==nums[i+1]:
                temp+=1
            else:
                ans=max(temp,ans)
                temp=0
        
# @lc code=end

