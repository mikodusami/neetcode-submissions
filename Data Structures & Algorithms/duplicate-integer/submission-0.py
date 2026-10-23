class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given an array nums
        # return True or False, true if element exists or has been seen
        # check every element
        # remember elements seen so far
        seen = set()
        for number in nums:
            if number in seen:
                return True
            seen.add(number)
        
        return False