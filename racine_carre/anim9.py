from manim import *

#manim -pql anim9.py Animation -o 32

class Animation(Scene):
    def construct(self):
        #Animation Heron
        A = 1236372
        rc = "{" + str(A) + "}"
        t = MathTex(f"\sqrt{rc}\n", font_size = 50)
        t.move_to([0,3.5,0])
        
        x = 20
        find=False
        old_rec=None
        prp=1100/A
        while not find:
            y = A/x
            rec=Rectangle(color=WHITE,height=y*prp,width=x*prp)
            rec.set_fill(BLUE,opacity=0.9)
            acc = Brace(rec,DOWN, buff=0.15)
            acc2 = Brace(rec, RIGHT, buff=0.15)
            t1 = MathTex(f"x = {round(x,2)}",font_size=38).next_to(acc,DOWN).shift(0.2*UP)
            t2 = MathTex(f"y = {round(y,2)}", font_size=38).next_to(acc2,RIGHT).shift(0.2*LEFT)
            rec_group = VGroup(
                rec,
                acc,
                acc2,
                t1,
                t2
            )
            if old_rec==None:
                t.next_to(rec_group,UP)
                self.play(Write(t))
                self.play(Create(rec_group, run_time=2))
                old_rec = rec_group
            else:
                self.play(Transform(old_rec,rec_group,run_time=0.9),
                          t.animate.next_to(rec_group,UP).shift(0.2*UP+0.2*LEFT))
            if round(x,2) == round(y,2):
                find=True
            x_ = (x+y)/2
            x = x_