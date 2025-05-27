class GameOfLife:
    def __init__(self, settings):
        self.rows = settings.rows
        self.cols = settings.cols
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def update(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_neighbors(r, c)
                if self.grid[r][c] == 1:
                    new_grid[r][c] = 1 if live_neighbors in [2, 3] else 0
                else:
                    new_grid[r][c] = 1 if live_neighbors == 3 else 0
        self.grid = new_grid

    def count_neighbors(self, r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            nr, nc = (r + dr) % self.rows, (c + dc) % self.cols
            count += self.grid[nr][nc]
        return count

    def toggle_cell(self, row, col):
        self.grid[row][col] = 1 - self.grid[row][col]
