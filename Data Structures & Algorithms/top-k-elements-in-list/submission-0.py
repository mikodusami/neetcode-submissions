class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Finds the frequency of each distinct element in the array and gets the top k most frequent distinct elements

        Args:
        nums: the array of which contains integer numbers
        k: the number of most frequent elements we need to return

        Return:
        result: an array of the top k most frequent elements in nums

        PreConditons:
        - nums contains duplicates
        - nums will always have at least one element
        - k will always be at least 1
        - k will always be less than the number of disinct elements in the array

        PostConditons:
        - there will always be an answer, never will return None
        - the result will contain k elements in nums
        """

        c = Counter(nums) # gets the frequencies of all numbers
        most_common_pairs = c.most_common(k) # gets the top k numbers
        return [pair[0] for pair in most_common_pairs]
