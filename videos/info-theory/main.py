from manimlib import * 


class WordleScene(Scene):
    def setup(self, n_letters=5):
        self.all_words = None
        self.n_letters = n_letters
        self.grid_height = 1
        
    def construct(self):
        self.setup()
        self.add_grid()
        
        
    def add_grid(self):
        buff = 0.1
        row = Square(side_length=1).get_grid(1, self.n_letters, buff=buff)
        grid = row.get_grid(6, 1, buff=buff)
        grid.set_height(1)
        grid.move_to(ORIGIN)
        grid.set_stroke(WHITE, 2)
        grid.words = VGroup()
        grid.pending_word = VGroup()
        #grid.add(grid.words, grid.pending_word)
        grid.pending_pattern = None
        grid.add_updater(lambda m: m)
        self.grid = grid
        self.add(grid)
