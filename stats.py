class Stats():
# статистика игры

    def __init__(self):
        self.reset_stats()
        self.run_game = True

    def reset_stats(self):
        self.guns_left = 2

