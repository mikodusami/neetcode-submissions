class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # INPUT:
        # nums = array of integers
        # k = maximum allowed distance between equal values

        # REMEMBER:
        # store each number's most recent index
        seen = {}

        for i, num in enumerate(nums):

            # INSPECT:
            # if we've seen this number before, check whether
            # the distance from its most recent index is <= k
            if num in seen and i - seen[num] <= k:

                # OUTPUT:
                # a valid nearby duplicate exists
                return True

            # REMEMBER:
            # update this number's most recent position
            seen[num] = i

        # OUTPUT:
        # no pair of equal values was within distance k
        return False