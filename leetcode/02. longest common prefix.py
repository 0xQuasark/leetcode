from typing import List
# https://leetcode.com/problems/longest-common-prefix/description/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

nums = [3,2,4]
target = 6
strs = ["flower","flow","flight", ""]
strs = ["dog","racecar","car", ""]
strs = ["cir","car"]
strs = ["a"]
strs = ["flower","flow","flight","fly"]
strs = ["abab","aba","abc"]
strs = ["flow", "flowering", "flonder"]


class Solution:
  def firstAttemptlongestCommonPrefix(self, strs: List[str]) -> str:
    """First answers, beats only 5%"""
    answer = ""
    strs = sorted(strs, key=lambda x: len(x), reverse=True)
    curr = strs[0]
    commons = []
    i = 0
    j = 0

    if (len(strs)) == 1:
      return curr

    for i in range(1, len(strs)):
      commons.append(0)
      # i, words in strs, starts at 1 cuz first is curr
      for j in range(0, len(strs[i])):
        # This is a new char in the string[i]
        if curr[0] != strs[i][0]:
          return ""
        
        if curr[j] == strs[i][j]:
          commons[i-1] += 1
        else:
          break
        #end j loop, j iterates to next char in word
      #end i loop, i iterates to next word in list
    
    # print(commons)
    if len(commons):
      numCommon = min(commons)

      for index in range(0, numCommon):
        answer += curr[index]
    else:
      answer = ""
    
    return answer

  def secondAttemptlongestCommonPrefix(self, strs: List[str]) -> str:
    """Second attempt, taking first comparing against last"""
    answer = ""
    if len(strs) == 1:
      return strs[0]
    
    strs = sorted(strs)

    first = strs[0]
    last = strs[-1]

    for i in range(0, len(first)):
      if (first[i] == last[i]):
        answer +=first[i]
      else:
        break

    for word in strs:
      if answer not in word:
        return ""

    return answer
  
  def thirdAttemptlongestCommonPrefix(self, strs: List[str]) -> str:
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    idx = 0

    while idx < len(first) and idx < len(last):
      if first[idx] == last[idx]:
        idx += 1
      else:
        break

    return first[0:idx]

s = Solution()
print(s.thirdAttemptlongestCommonPrefix(strs))



# Thoughts
# July 1 2023
# firstAttemptlongestCommonPrefix
#   Brute forced this, lots of test cases in leetcode, mixed me up
#   ppl on leetcode ask why this is marked as easy.. 
#   it's just arrays and brute force really, no complex algo if you don't want
#   but.. i agree, to do this efficiently requires some more understanding
# 
# secondAttemptlongestCommonPrefix (second attempt)
#   much better for me. inspired by https://leetcode.com/problems/longest-common-prefix/solutions/3174307/well-explained-code-using-strings-in-java/
#   the trick was the sorted method. it returns 

# thirdAttemptlongestCommonPrefix
# this was just taking the same logic from the explanation

