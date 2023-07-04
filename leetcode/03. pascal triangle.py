# https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# 
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 
# Example 2:
# Input: numRows = 1
# Output: [[1]]


from typing import List

nums = [3,2,4]
target = 4


class Solution:
  def firstGenerate(self, numRows: int) -> List[List[int]]:
    answer = []
    # Pascals triangle's first row has 1 element, second row 2 elements, etc.

    if numRows < 1:
      return 0
    elif numRows == 1:
      return 1
    elif numRows == 2:
      answer.append(1)
      return answer
    elif numRows >= 3:
      currentRow = 2
      previousRow = 1
      idx = 3
      answer += [[1]]
      answer += [[1,1]]

      while idx <= numRows:
        newList = []
        newList += [1]
        for i in range(1, numRows-1):
          newSum = 0
          newSum = answer[previousRow][i-1] + answer[previousRow][i]
          newList.append(newSum)
          previousRow += 1
          i += 1
        newList += [1]
        answer.append(newList)
        idx += 1
      
    return answer




s = Solution()
print(s.firstGenerate(target))
