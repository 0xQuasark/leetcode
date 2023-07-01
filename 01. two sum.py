from typing import List
# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the 
# same element twice.
# You can return the answer in any order.


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    answer = []
    for i in range(0, len(nums) - 1): # i is iterating through each number, up to the penultimate one
      for j in range(i+1, len(nums)):   # j iterates through the subsequent number to i, up to array end
                                      # j is the seeker element, so moves through the rest of the array
                                      # searching for something that can be added dto i to add to target
        if nums[i] + nums[j] == target: # if current number(i) plus seeker's number (j) == target, we get answer
          # condition = True          # TO DO save position i and j, that's the answer
          answer.append(i)
          answer.append(j)
          print (i,j)


    return answer




# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

s = Solution()
print(s.twoSum(nums, target))