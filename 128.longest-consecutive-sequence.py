#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        st= set()
        max_count = 1
        for i in nums:
            st.add(i)
        for i in st:
            if i-1 not in st:
                count = 1
                while i+1 in st:
                    count+=1
                    i+=1
                max_count = max(max_count,count)
        return max_count        
# @lc code=end

