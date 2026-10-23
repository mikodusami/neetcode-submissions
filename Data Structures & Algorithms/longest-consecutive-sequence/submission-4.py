class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 1
        for number in nums:
            current, x = 1, number
            if x + 1 in s:
                continue
            while x - 1 in s:
                current += 1
                longest = max(longest, current)
                x -= 1
                
            current = 0
        
        return longest if nums else 0