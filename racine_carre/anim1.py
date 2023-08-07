from manim import *

#manim -pql anim1.py Animation

class Animation(Scene):
    def construct(self):
        plane = NumberPlane()
        #self.add(plane)

        square1 = Square(side_length=1.8).rotate(PI/2)
        square1.set_fill(color="#00B5F5",opacity=0.7)
        
        square1_point = VGroup(
            Dot(point=square1.get_critical_point(DL),radius=0.02,color='#FFFFFF'),
            Dot(point=square1.get_critical_point(UL),radius=0.02,color='#FFFFFF'),
            Dot(point=square1.get_critical_point(DR),radius=0.02,color='#FFFFFF'),
            Dot(point=square1.get_critical_point(UR),radius=0.02,color='#FFFFFF')
        ) # Down/Up Left ; Down/Up Right
        square1_line = VGroup(
            Line(start=square1_point[0], end=square1_point[2]),
            Line(start=square1_point[0], end=square1_point[1]),
            Line(start=square1_point[1], end=square1_point[3]),
            Line(start=square1_point[2], end=square1_point[3])
        )
        text1 = MathTex(r'c',font_size=43).next_to(square1_line[0],DOWN)
        
        #Ligne1
        self.play(Create(square1_point[0]),Create(square1_line[0], run_time=1.5))
        self.play(FadeIn(text1, run_time=0.3))
        
        #Ligne2
        self.wait(2)
        line1_cop=square1_line[0].copy()
        self.play(Transform(line1_cop,square1_line[1]))
        text2=text1.copy()
        self.play(FadeIn(text2.next_to(square1_line[1],LEFT), run_time=0.3))
        
        #Carré
        self.wait(2)
        self.play(Create(square1))
        self.add(square1_point[1])

        #Formule
        eq1 = MathTex(r"Aire\space=\space c^{2}",font_size=45).next_to(square1,RIGHT)
        self.play(Write(eq1))
        self.wait(2)
        
        #Regroupement
        square1_groupe = VGroup(
            square1,
            text1,
            text2,
            eq1,
            square1_line,
            square1_point,
            line1_cop
        )
        self.play(ScaleInPlace(square1_groupe,0.6))
        self.play(square1_groupe.animate.shift(4.5*LEFT))
        self.wait(1.5)

        square2 = Square(side_length=1.8).move_to([1,0,0])
        square2.set_fill(ORANGE,opacity=0.75)
        text3 = MathTex(r"\sqrt{Aire}", font_size=42).move_to(square2.get_critical_point((0,0,0)))
        
        #Carré 2 et Texte Aire
        self.play(Create(square2))
        self.play(Write(text3))
        self.wait(1.7)

        #Texte
        """
        #Ajout 4 c autour du carré
        text4 = VGroup()
        for i in [UP,RIGHT,DOWN,LEFT]:
            txt = MathTex(r"c", font_size=40)
            txt.next_to(square2,i)
            self.play(FadeIn(txt,run_time=0.3))
            text4.add(txt)
        """
        accolade = Brace(square2,RIGHT,buff=0.16)
        text4 = MathTex(r"c",font_size=40).next_to(accolade,(RIGHT-0.47*RIGHT))
        self.play(FadeIn(accolade))
        self.play(FadeIn(text4))
        self.wait(2)

        #Groupe 2
        square2_groupe = VGroup(
            text3,
            text4,
            accolade,
            square2
        )
        self.play(square2_groupe.animate.shift(2.7*RIGHT),
                  ScaleInPlace(square1_groupe,1/0.6))
        self.play(square1_groupe.animate.shift(2*UP),
                  square2_groupe.animate.shift(2*UP))
        self.add(square2_groupe[0])
        self.wait(2)
        
        #Texte Recap
        text5_v1 = MathTex(r"x^{2}",font_size=60,color="#00DAFF").move_to([-4.5,-1.5,0])
        text5_v2 = MathTex(r"c\to Aire",font_size=60,color="#00DAFF").move_to([-4.5,-1.5,0])

        text6_v1 = MathTex(r"\sqrt{x}",font_size=60,color="#FFF300").move_to([4,-1.5,0])
        text6_v2 = MathTex(r"Aire\to c",font_size=60,color="#FFF300").move_to([4,-1.5,0])

        self.play(Write(text5_v1,run_time=1.2),Write(text6_v1,run_time=1.2,lag_ratio=0.85))
        self.wait(1)
        self.play(FadeOut(text5_v1,run_time=1),FadeIn(text5_v2,run_time=1.3,lag_ratio=0.4))

        self.wait(2.5)
        
        self.play(FadeOut(text6_v1,run_time=1),FadeIn(text6_v2,run_time=1.3,lag_ratio=0.4))

        self.wait(4)

        #Disparition
        all = VGroup(square1_groupe,
                     square2_groupe,
                     text5_v2,
                     text6_v2)
        self.play(FadeOut(all,run_time=2))
        self.wait(1)

        
