class Solution:
    def maxDepth(self, s: str) -> int:
        longest = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                longest = max(longest, len(stack))
                stack.pop()


        return longest