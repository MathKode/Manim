from manim import *

#manim -pql anim4.py Animation

class Animation(Scene):
    def construct(self):
        racine1 = MathTex(r"\sqrt{51} \space = \space ?", font_size=50).move_to([8,3,0]).rotate(-PI/9)
        self.play(racine1.animate.move_to([5.5,3,0]))
        self.wait(1)
        """
        [
          "", -> Ligne
          [ "", ""] -> Changement sur la meme ligne 
        ]
        """
        txt = [
            [
                r"x_0 = 1"
            ],
            [   
                r"x_1 = \frac{x_0+\frac{Aire}{x_0}}{2}",
                r"x_1 = \frac{1+\frac{51}{1}}{2}",
                r"x_1 = \frac{52}{2}",
                r"x_1 = 26"
            ],
            [
                r"x_2 = \frac{x_1+\frac{Aire}{x_1}}{2}",
                r"x_2 = \frac{26+\frac{51}{26}}{2}",
                r"x_2 = \frac{727}{52}",
                r"x_2 = 13,98"
            ],
            [
                r"x_3 = \frac{x_2+\frac{Aire}{x_2}}{2}",
                r"x_3 = \frac{13,98+\frac{51}{13,98}}{2}",
                r"x_3 = \frac{666433}{75608}",
                r"x_3 = 8,81"
            ],
            [
                r"x_4 = \frac{x_3+\frac{Aire}{x_3}}{2}",
                r"x_4 = \frac{8,81+\frac{51}{8,81}}{2}",
                r"x_4 = 7,30"
            ],
            [
                r"x_5 = \frac{x_4+\frac{Aire}{x_4}}{2}",
                r"x_5 = \frac{7,30+\frac{51}{7,30}}{2}",
                r"x_5 = 7,1432"
            ],
            [
                r"x_6 = \frac{x_5+\frac{Aire}{x_5}}{2}",
                r"x_6 = \frac{7,1432+\frac{51}{7,1432}}{2}",
                r"x_6 = 7,1414"
            ]
        ]
        position=[0,3.4,0]
        text_group = VGroup()
        for line in txt:
            old = None
            for modif in line:
                text = MathTex(modif, font_size=43)
                text.move_to(position)  
                if old == None:
                    self.play(Write(text, run_time=1))
                    old = text
                    self.wait(2.5)
                else :
                    self.play(Transform(old, text, run_time=1))
                    self.wait(1)
                text_group.add(old)
            position[1] = position[1] - 1.1
        self.wait(2)
        self.play(text_group.animate.shift(5*LEFT),
                  racine1.animate.shift(5.3*LEFT))
        
        text1 = MathTex(r"f(",r"x_n",r")=",r"x_n^{2}", font_size=60)
        #text1.set_color_by_tex("x_n",YELLOW)
        text1.set_opacity_by_tex("x_n",1)
        text1.move_to([0,0,0])

        self.play(FadeIn(text1))
        self.wait(1)

        result=[1, 676, 195.44, 77.61, 53.29, 51.02, 51]
        couleur = ["#ff0000","#ffa700","#ffa700","#fff400","#a3ff00","#a3ff00", "#2cba00"]
        tour=0
        for t in text_group:
            txt = t.copy()
            self.play(txt.animate.move_to([0,0,0]))
            result_txt=MathTex(str(result[tour]))
            result_txt.set_color(couleur[tour])
            result_txt.set_opacity(1)
            result_txt.move_to([5,t.get_critical_point([0,0,0])[1],0])
            self.play(Transform(txt,result_txt))
            tour+=1
        
        text2 = MathTex(r"\sqrt{51} \space = \space 7,1414", font_size=65).move_to([0,-2,0])
        self.wait(1.5)
        self.play(Write(text2, run_time=2))
        self.wait(2)











        