class GameOfLife:
    """
      Logika gry w życie Conwaya.

      :param settings: Obiekt ustawień gry.
      :type settings: GameSettings
      """

    def __init__(self, settings):
        """
               Inicjalizuje nową siatkę gry na podstawie ustawień.
        """
        self.rows = settings.rows
        self.cols = settings.cols
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def update(self):
        """
                Aktualizuje stan siatki według reguł Conwaya.
                """
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
        """
              Liczy żywych sąsiadów dla komórki (r, c).

              :param r: Wiersz komórki.
              :type r: int
              :param c: Kolumna komórki.
              :type c: int
              :return: Liczba żywych sąsiadów.
              :rtype: int
              """
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            nr = (r + dr) % self.rows
            nc = (c + dc) % self.cols
            count += self.grid[nr][nc]
        return count

    def toggle_cell(self, row, col):
        """
              Zmienia stan komórki (żywa ↔ martwa).

              :param row: Wiersz.
              :type row: int
              :param col: Kolumna.
              :type col: int
              """
        self.grid[row][col] = 1 - self.grid[row][col]
