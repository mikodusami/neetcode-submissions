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

        # gets the frequencies of all numbers
        dictionary = defaultdict(int)
        for number in nums:
            dictionary[number] += 1
        
        # number: frequency
        # bucketArray[frequency] = [number]
        bucket_array = [[] for _ in range(len(nums) + 1)]
        for number, freq in dictionary.items():
            bucket_array[freq].append(number)

        # gets the top k numbers
        result = []
        for bucket in reversed(bucket_array):
            i = 0
            while i < len(bucket) and len(result) < k:
                result.append(bucket[i])
                i += 1

        return result
        
