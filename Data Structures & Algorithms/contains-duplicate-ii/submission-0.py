class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        dupes = []
        seen = defaultdict()
        # find all duplicates
        for i in range(len(nums)):
            if nums[i] in seen:
                dupes.append((seen[nums[i]], i))
                del seen[nums[i]]
            seen[nums[i]] = i

        # combine indices until one matches
        for dupe in dupes:
            if abs(dupe[0] - dupe[1]) <= k:
                return True
        
        return False