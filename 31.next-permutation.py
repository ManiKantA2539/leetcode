#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums [i-1]:
                point = i-1
                break
        if point==-1:
            nums.reverse()
            return

        for i in range(len(nums)-1,point,-1):
            if nums[i]>nums[point]:
                nums[i],nums[point] = nums[point],nums[i]
                break
        nums[point+1:] = reversed(nums[point+1:])
        

        

# @lc code=end

