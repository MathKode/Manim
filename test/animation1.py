from manim import *

#manim -pql animation1.py animation1
#-p : play
#-qh : high quality
#-ql : low quality

#https://www.tug.org/mactex/mactex-download.html
#https://3b1b.github.io/manim/getting_started/example_scenes.html#textexample

class animation1(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(RED,opacity=0.5)

        info1 = Text("This is a Circle", t2w={"C":BOLD}, t2c={"Circle":YELLOW})
        
        #coordonné bas du cercle centre
        gps=circle.get_critical_point(DOWN)
        print(gps)
        info1.move_to(gps+DOWN/2)

        info2 = MathTex(r'A = \pi\space\ast\space r^2').move_to(gps+DOWN/2)

        info3 = MathTex(r'A = c^2')

        square = Square()
        square.rotate(PI/4)
        square.set_fill(BLUE,opacity=0.8)

        self.play(Create(circle, run_time=2), Write(info1))
        self.wait(1)
        self.play(Unwrite(info1, reverse=False),FadeIn(info2, lag_ratio=0.2))
        self.wait(1)
        self.play(Transform(circle,square, run_time=1.5), info2.animate.shift(DOWN/2))
        info3.move_to(info2.get_critical_point((0,0,0)))
        self.play(TransformMatchingShapes(info2,info3))
        self.wait(2)
        self.play(Uncreate(circle, run_time=2.2), FadeOut(info3, run_time=1.5, lag_ratio=0.5))
