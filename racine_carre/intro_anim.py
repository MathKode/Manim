from manim import *
from math import sqrt

#manim -pql intro_anim.py Animation

class Animation(Scene):
    def construct(self):
        t = MathTex(r"\sqrt{x}",font_size=130).move_to([0,0,0])
        self.play(Write(t,run_time=2))
        self.play(t.animate.shift(2*UP))

        self.wait(0.5)
        ax = Axes(x_range=[0,100,25],y_range=[0,12.49,2.5],x_length=5,y_length=2.5, x_axis_config = {"label_direction" : DOWN, "include_numbers": True},y_axis_config = {"label_direction" : LEFT, "include_numbers": True})
        ax.move_to([0,-1.2,0])
        curve = ax.plot(lambda x: sqrt(x), color=RED)
        self.play(FadeIn(ax,run_time=0.8))
        self.play(Create(curve,run_time=2.8))
        self.wait(10)