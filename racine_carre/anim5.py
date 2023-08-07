from manim import *

#manim -pql anim5.py Animation

class Animation(Scene):
    def construct(self):
        #self.add(NumberPlane())
        text1 = Text("Moyenne Arithmétique", font_size=40).move_to([0,3.4,0])
        self.play(Write(text1))

        p1 = Dot([-4,-1,0], radius=0.05)
        p2 = Dot([-3,-1,0], radius=0.05)
        p3 = Dot([-3,1,0], radius=0.05)

        l1 = Line(p1,p2,buff=1)
        l2 = Line(p2,p3,buff=1)
        
        t1 = Text("x",font_size=33).next_to(l1,DOWN)
        t2 = Text("y",font_size=30).next_to(l2,RIGHT)

        p4=Dot([-1,1,0])
        p5=Dot([0,1,0])
        p6=Dot([2,1,0])

        l3 = Line(p4,p5)
        l4 = Line(p5,p6)

        t3 = Text("x",font_size=33).next_to(l3,DOWN)
        t4 = Text("y",font_size=30).next_to(l4,DOWN)

        l5 = CurvedArrow([2.2,0.95,0],[2.2,-0.95,0],radius=-1.7)

        t5 = MathTex(r"\overline{x} = \frac{x+y}{2}",font_size=45).next_to(l5,RIGHT).shift(RIGHT*0.25)

        p7 = Dot([-1,-1,0])
        p8 = Dot([0.5,-1,0])
        p9 = Dot([2,-1,0])

        l6 = Line(p7,p8)
        l7 = Line(p8,p9)

        t6 = Text("x'",font_size=33).next_to(l6,DOWN)
        t7 = Text("y'",font_size=30).next_to(l7,DOWN)

        t8 = Text("Donc si x est trop petit, sa valeur augmente \n(et inversement, si il est trop grand sa valeur diminue)",font_size=40).move_to([0,-3,0])

        #self.add(text1,p1,p2,p3,l1,l2,t1,t2, p4,p5,p6,l3,l4, t3, t4,l5, t5, p7, p8, p9, l6, l7, t6, t7, t8)
        self.wait(1)

        self.play(FadeIn(p1), FadeIn(p2))
        self.play(Create(l1))
        self.play(FadeIn(t1))
        self.wait(0.5)
        self.play(FadeIn(p3))
        self.play(Create(l2))
        self.play(FadeIn(t2))

        self.wait(1)

        x1 = VGroup(
            p1,
            p2,
            l1,
            t1
        ).copy()
        x2 = VGroup(
            p4,
            p5,
            l3,
            t3
        ).copy()
        x3 = VGroup(
            p7,
            p8,
            l6,
            t6
        ).copy()

        y1 = VGroup(
            p2,
            p3,
            l2,
            t2
        ).copy()
        y2 = VGroup(
            p5,
            p6,
            l4,
            t4
        ).copy()
        y3 = VGroup(
            p8,
            p9,
            l7,
            t7
        ).copy()



        self.play(Transform(x1,x2))
        self.wait(0.5)
        self.play(Transform(y1,y2))

        self.wait(2)

        self.play(Create(l5))
        self.play(FadeIn(t5))

        self.wait(1)

        x2_ = x1.copy()
        y2_ = y1.copy()
        self.play(Transform(x2_,x3))
        self.wait(0.5)
        self.play(Transform(y2_,y3))

        self.wait(2)

        self.play(Write(t8))
        self.wait(2)
        
