from manimlib import * 


class WordleScene(InteractiveScene):
    n_letters = 5
    def setup(self):
        self.all_words = None