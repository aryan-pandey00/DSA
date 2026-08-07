from collections import deque

class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0] * m for _ in range(n)]
        
        # Sort sources by color descending
        sources.sort(key=lambda x: -x[2])
        
        q = deque()
        
        # Initialize
        for r, c, color in sources:
            grid[r][c] = color
            q.append((r, c, color))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # BFS
        while q:
            r, c, color = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                    grid[nr][nc] = color
                    q.append((nr, nc, color))
        
        return grid