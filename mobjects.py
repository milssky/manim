from manim import *


class CreatingMObjects(Scene):
    def construct(self):
        star = Star()
        self.add(star)
        self.wait(1)
        self.remove(star)
        self.wait()


class Shapes(Scene):
    def construct(self):
        star = Star()
        square = Square()
        circle = Circle()

        circle.shift(LEFT)
        star.shift(UP)
        square.shift(RIGHT)

        self.add(star, square, circle)
        self.wait(1)


class ShapesPlacement(Scene):
    def construct(self):
        star = Star()
        square = Square()
        circle = Circle()

        star.move_to(LEFT * 2)  # сдвинуть звезду на две единицы влево
        square.next_to(star, LEFT)  # поставить квадрат слева от звезды
        # выровнять левую границу круга с левой границей звезды
        circle.align_to(star, LEFT)

        self.add(star, square, circle)
        self.wait(1)


class ShapesStyle(Scene):
    def construct(self):
        star = Star().shift(LEFT)
        square = Square().shift(RIGHT)
        circle = Circle().shift(UP)

        star.set_color(RED)
        square.set_fill(color=YELLOW, opacity=0.5)
        circle.set_stroke(PINK, width=20)

        self.add(circle, star, square)
        self.wait(1)
