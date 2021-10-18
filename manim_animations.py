from manim import *

class ShapeAnimation(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(FadeIn(square))
        self.play(Rotate(square, PI/4))
        self.play(FadeOut(square))
        self.wait(1)


class ShapePropsAnimation(Scene):
    def construct(self):
        square = Square().set_fill(BLUE, opacity=1.0)
        self.add(square)

        self.play(square.animate.set_fill(RED))
        self.wait(1)

        self.play(square.animate.shift(UP).rotate(PI/3))
        self.wait(1)


class ShapeRunTimeAnimation(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(square.animate.shift(UP), run_time=3)
        self.wait()
