class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Summary: Finding the maximum area between any two heights

        Args:
        heights: an array of numbers where array[i] is the height of one bar

        Return:
        int: the maximum area between any two heights

        PreConditons:
        - heights contains duplicates
        - heights will always have at least two elements
        - heights[i] can be 0 -> maximum 10,000

        PostConditions:
        - a valid integer will always be returned

        Examples:
        >> maxArea([1, 7, 2, 5, 4, 7, 3, 6]) => 36 because heights[1] and heights[7] have the maximum area 
        """


        def computeArea(indexOne, indexTwo):
            """
            preconditon: indexTwo will be greater than indexOne
            - indexOne and indexTwo will be between 0 and len(heights) inclusive
            """
            heightOne = heights[indexOne]
            heightTwo = heights[indexTwo]
            width = indexTwo - indexOne
            return width * min(heightOne, heightTwo)
        
        i, j = 0, len(heights) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, computeArea(i, j))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
          

        return max_area








