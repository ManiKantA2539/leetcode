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
        res=[]
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start,len(nums)):
                nums[start],nums[i] = nums[i],nums[start]
                backtrack(start+1)
                nums[start],nums[i] = nums[i],nums[start]
        backtrack(0)
        num = int("".join(map(str,nums)))
        temp = [int("".join(map(str,x))) for x in res]
        temp.sort()
        ans = []
        for i in temp:
            if i>num:
                ans = [int(digit) for digit in str(i)]
                break
        if(ans==[]):
            nums= [int(digit) for digit in str(temp[0])]
        else:
            nums= ans
        return        

# @lc code=end

