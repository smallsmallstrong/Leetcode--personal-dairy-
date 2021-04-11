"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
"""
dict.keys()--> This method returns a list of all the available keys in the dictionary.
dict.get --> The get() method is used to avoid such situations. This method returns the value for the given key,
if present in the dictionary. 
If not, then it will return None (if get() is used with only one argument).
## Array, Hash Table
"""

class Solution:
    def twoSum(self, nums, target):
        dict = {}
        l = len(nums)
        for i in range(l):
            # judge if target-nums[i] is in the dict
            if (target-nums[i]) in dict.keys():
                # if target-nums[i] is in the dict, than return the first index(target-nums[i])
                return [dict.get(target-nums[i]), i]
            else:
                # if target value just one number value of the dict
                dict[nums[i]] = i
        # after the loop no matched pair, then return none
        return(None)

nums = [2,7,11,15]
target = 9

sol = Solution()


