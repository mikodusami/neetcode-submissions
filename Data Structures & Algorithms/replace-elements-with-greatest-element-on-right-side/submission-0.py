class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greater_element = arr[-1]
        last_seen_element = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            greater_element = max(greater_element, last_seen_element)
            last_seen_element = arr[i]
            arr[i] = greater_element
        
        arr[-1] = -1
        return arr
            