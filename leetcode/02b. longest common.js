strs = ["flower","flow","flight", ""]
strs = ["dog","racecar","car", ""]
strs = ["cir","car"]
strs = ["a"]
strs = ["abab","aba","abc"]
strs = ["flower","flow","flight","fly"]
strs = ["flow", "flowering", "flownder"]


class Solution {
 longestCommonPrefix(strs) {
    strs.sort();
    let first = strs[0];
    let last = strs[strs.length - 1];
    let idx = 0;

    while (idx < first.length && idx < last.length) {
      if (first[idx] === last[idx]) {
        idx++;
      } else {
        break;
      }
    }

    return first.substring(0, idx);
  }
}

let s = new Solution();
console.log(s.longestCommonPrefix(strs))
