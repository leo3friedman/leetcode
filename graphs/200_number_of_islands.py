# Runtime 284ms, Beats 66.60% of users with Python3
# Memory 18.63MB, Beats 92.47%of users with Python3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 
        rows, cols = len(grid), len(grid[0])  
        islands = 0 

        def in_grid(r,c):
            return (r >= 0 and r < rows and
                    c >= 0 and c < cols)

        def bfs(r,c):
            queue = [(r,c)]
            grid[r][c] = '0'
            while queue:
                r, c = queue.pop(0)
                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    next_r, next_c = r+dr, c+dc
                    if in_grid(next_r, next_c) and grid[next_r][next_c] == '1':
                        grid[next_r][next_c] = '0'
                        queue.append((next_r, next_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r,c) 
                    islands += 1
                   
        return islands
