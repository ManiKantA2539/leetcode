#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0] * len(nums)
        pos=0
        neg=1
        for i in range(0,len(nums)):
            if(nums[i]>0):
                ans[pos]=nums[i]
                pos+=2
            else:
                ans[neg]=nums[i]
                neg+=2
       
        return ans
        
# @lc code=end

