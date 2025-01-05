class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        queue = []
        count = 0
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "1":  
                    count += 1
                    grid[r][c] = "0"
                    queue.append((r, c))
                    while queue:
                        cr, cc = queue.pop(0)
                        children = [(cr + dr, cc + dc) for dr, dc in directions
                                    if 0 <= cr + dr < len(grid) and 0 <= cc + dc < len(grid[0])]
                        for child in children:
                            if grid[child[0]][child[1]] == "1":
                                grid[child[0]][child[1]] = "0"
                                queue.append(child)
        return count
