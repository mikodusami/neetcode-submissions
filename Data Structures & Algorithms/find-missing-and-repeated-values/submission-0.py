class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a = -1
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in seen and a == -1:
                    a = grid[i][j]
                seen.add(grid[i][j])


        b = -1
        for i in range(1, rows**2 + 1):
            print(i, end="")
            if i not in seen:
                b = i
            if b != -1:
                break
        
        return [a, b]