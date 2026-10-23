class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        original_color = image[sr][sc]
        if image[sr][sc] == color:
            return image
        
    
        def dfs(i, j):
            if i > len(image) - 1 or j > len(image[0]) - 1 or i < 0 or j < 0:
                return 
            if (i, j) in visited:
                return
            if image[i][j] != original_color:
                return
            print(i, j)
            image[i][j] = color
            visited.add((i, j))
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        dfs(sr, sc)
        
        return image