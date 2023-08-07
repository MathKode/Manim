from manim import *

class Animation(Scene):
    def construct(self):
        t = MathTex(r"\sqrt{x}",font_size=150).move_to([0,0,0])
        self.add(t)