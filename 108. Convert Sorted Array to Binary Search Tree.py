# May 27 2020
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode: # thought of construct left and right respectively
        if not nums:
            return None
        length = len(nums)
        mid = length//2
        return TreeNode(val=nums[mid],left=self.sortedArrayToBST(nums[:mid]),right=self.sortedArrayToBST(nums[mid+1:]))
        