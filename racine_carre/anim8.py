from manim import *

#manim -pql anim8.py Animation

class Animation(Scene):
    def construct(self):
        txt = MathTex(r"\log{(x\space * \space x)} \space = \space \log{(x)} \space + \space \log{(x)}", font_size=100).move_to([0,0,0])
        self.wait(1)
        self.play(Write(txt, run_time=3))
        self.wait(15)
        self.play(FadeOut(txt))
        self.wait(0.1)