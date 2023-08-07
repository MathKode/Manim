from manim import *

#manim -pql anim3.py Animation

class Animation(Scene):
    def construct(self):
        #Généralisation de la formule
        #self.add(NumberPlane())

        text1 = MathTex(r"x_{n+1}", r"\space = \space", r"{x_n", r"+", r"{Aire", r"\over", r"x_n}", r"\over", r"2}",font_size=65)
        text1.set_color_by_tex(r"x_n","#37A5FF")
        text1.set_opacity_by_tex(r"x_n",1)
        text1.set_color_by_tex(r"x_{n+1}","#37A5FF")
        text1.set_opacity_by_tex(r"x_{n+1}",1)
        text1.set_color_by_tex(r"Aire","#FFC300")
        text1.set_opacity_by_tex(r"x_{n+1}",1)
        text1.move_to([0,0,0])

        self.play(Write(text1))
        self.wait(1.5)
        self.play(text1.animate.shift(2.2*UP))

    

