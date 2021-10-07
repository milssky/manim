from manim import *


class SquareToStar(Scene):
    def construct(self):
        square = Square()
        square.set_fill(GREEN, opacity=0.5)
        star = Star(outer_radius=2, color = BLUE)
        self.play(Create(square)) 
        self.play(Transform(square, star))
        self.play(FadeOut(square))

