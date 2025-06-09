class GameSettings:
    """
    Przechowuje ustawienia gry.

    :param rows: Liczba wierszy siatki.
    :type rows: int
    :param cols: Liczba kolumn siatki.
    :type cols: int
    :param speed: Prędkość odświeżania (w milisekundach).
    :type speed: int
    """

    def __init__(self, rows=30, cols=30, speed=100):
        self.rows = rows
        self.cols = cols
        self.speed = speed  # ms per frame
