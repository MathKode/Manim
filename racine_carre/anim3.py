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
        self.play(text1.animate.shift(1*UP))

        #self.wait(0.5)
        surrounding = SurroundingRectangle(text1[2],YELLOW,buff=0.05, stroke_width=6)
        self.play(Create(surrounding))
        self.wait(1)
        
        
        text2 = MathTex(r"x_{0}", r"\space = ... \space \space \space",r"\textit{(Nombre choisi)}")
        text2.next_to(text1,UP).shift(UP*0.5)
        text2.set_color_by_tex(r"x_{0}","#37A5FF")
        text2.set_opacity_by_tex(r"x_{0}",1)
        text2.set_color_by_tex(r"Nombre","#83bd00")
        text2.set_opacity_by_tex(r"Nombre",0.8)
        self.play(Write(text2, run_time=1))
        self.play(FadeOut(surrounding))

        self.wait(1)

        surrounding1 = SurroundingRectangle(text1[4:7],YELLOW,buff=0.05, stroke_width=6)
        self.play(Create(surrounding1))
        self.wait(1)

        text3 = text1[4:7].copy()
        self.add(text3)
        self.play(text3.animate.move_to([-3.5,-1.5,0]))
        self.play( FadeOut(surrounding1))

        self.wait(1)

        text4 = MathTex("= \space y", font_size=55).next_to(text3, RIGHT)
        self.play(Write(text4))

        surrounding2 = SurroundingRectangle(text1[2:],YELLOW,buff=0.05, stroke_width=6)
        self.play(Create(surrounding2))
        self.wait(1)

        text5 = text1[2:].copy()
        self.add(text5)
        self.play(text5.animate.move_to([3,-1.5,0]))
        self.play( FadeOut(surrounding2))

        self.wait()
        text6 = MathTex(r"{x",r"+",r"y",r"\over 2}", font_size=55)
        text6.move_to(text5.get_critical_point([0,0,0]))
        text6.set_color_by_tex(r"x","#37A5FF")
        text6.set_opacity_by_tex(r"x",1)
        text6.set_color_by_tex(r"y","#FFC300")
        text6.set_opacity_by_tex(r"y",1)
        self.play(Transform(text5,text6, run_time=1))

        text7 = MathTex("= \space x'", font_size=55).next_to(text6, RIGHT)
        self.play(Write(text7))



