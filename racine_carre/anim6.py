from manim import *

#manim -pql anim6.py Animation

class Animation(Scene):
    def construct(self):
        #Logarithme
        txt = [
            [
                r"c^2 \space =\space A",
                r"\log{(c^2)} \space =\space \log{(A)}",
                r"\log{(c*c)} \space =\space \log{(A)}",
                r"\log{(c)} + \log{(c)} \space =\space \log{(A)}",
                r"2 * \log{(c)} \space =\space \log{(A)}",
                r"\log{(c)} \space =\space \frac{\log{(A)}}{2}",
                r"c \space =\space 10^{\frac{\log{(A)}}{2}}",
                r"\sqrt{A} \space =\space 10^{\frac{\log{(A)}}{2}}"
            ]
        ]
        position=[0,3.5,0]
        text_group = VGroup()
        for line in txt:
            old = None
            for modif in line:
                text = MathTex(modif, font_size=38)
                text.move_to(position)  
                if old == None:
                    self.play(Write(text, run_time=1))
                    old = text.copy()
                    self.wait(2)
                else :
                    self.play(Transform(old, text, run_time=1))
                    old = old.copy()
                    self.wait(2)
                text_group.add(old)
                position = position + DOWN
        self.wait(2)

        s = SurroundingRectangle(text_group[-1],YELLOW)
        self.play(Create(s))
        self.play(FadeOut(s))

        self.wait(2)