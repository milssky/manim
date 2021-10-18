from manim import *


class SquareToCircleScene(Scene):
    def construct(self):
        square = Square().set_fill(BLUE, opacity=1.0)
        circle = Circle().set_fill(RED, opacity=1.0)
        self.add(square)
        self.play(Transform(square, circle), run_time=2)
        self.wait()
