# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".



# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
#
#
# Clarifying Question:
#
# Do we need to return the longst common prefix for all strings in the input array? I'm assuimg yes looking at the 1st example
#
# Approach:
#
# We need to go over each string char simultaneosuly using same index checking if they match and updating out prefix string that we will maintain. One thing to take care of is we will only check till the length of the minimum string. For that we need to calculate the length of min string first.ArithmeticError
#
#   TC: O(n * m) where n = len(strs) and m is minimum string length
#   SC: O(1)

def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""

    min_string_len = 0
    i = 0

    for string in strs:
        min_string_len = min(min_string_len, len(string))

    while i < min_string_len:
        for s in strs:
            if s[i] != strs[0][i]:
                return prefix

        prefix += s[i]
        i += 1

    return prefix
