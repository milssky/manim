from manim import *


class SquareToStar(Scene):
    def construct(self):
        square = Square()
        square.set_fill(GREEN, opacity=0.5)
        self.play(Create(square))
