"""46. Permutations
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
# 解法一
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        if not nums:
            return []
        self.recursive(nums, [])
        return self.ans

    def recursive(self, nums, res):
        if not nums:
            self.ans.append(res)
        else:
            for i in range(len(nums)):
                self.recursive(nums[:i] + nums[i+1:], res + [nums[i]])
            
# 解法二
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if nums:
            self.dfs(nums, 0, ret)
        return ret

    def dfs(self, nums, begin, ret):
        if begin > len(nums)-1:
            ret.append(nums[:])
            return
        for i in range(begin, len(nums)):
            nums[begin], nums[i] = nums[i], nums[begin]
            self.dfs(nums, begin+1, ret)
            nums[begin], nums[i] = nums[i], nums[begin]
