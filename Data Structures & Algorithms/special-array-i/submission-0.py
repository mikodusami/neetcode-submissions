class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # what is parity

        def testParity(a, b):
            if a % 2 == 0 and b % 2 == 1:
                return True
            elif a % 2 == 1 and b % 2 == 0:
                return True
            return False
        
        for i in range(len(nums) - 1):
            if not testParity(nums[i], nums[i + 1]):
                return False
        
        return True