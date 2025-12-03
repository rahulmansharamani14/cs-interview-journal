# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 10^5.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


"""
Approach 1: Stack to store digits

- Traverse through the input string
- If char is not "]", append char to the stack
- else: 
    - build the substr -> pop the char from stack until you hit "[" (while preserving the order)
    - build the k number -> pop the char from stack until stack is empty (while preserving the order)
    - compute the new string as k * substr and store the new string onto to the stack
- At the end return the string by poping from the stack (while preserving the order)

TC: O(n) for traversing through the entire string, ignoring the time to build the string
SC: O(n) in worst case for strong in extra stack data structure


"""


def decodeString(s: str) -> str:
    stack = []
    
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            substr = ""

            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop() #removing "["

            k = ""

            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            stack.append(int(k) * substr)
    
    res = ""

    while stack:
        res = stack.pop() + res
    return res
            


