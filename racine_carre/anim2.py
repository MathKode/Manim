from manim import *

#manim -pql anim2.py Animation

class Animation(Scene):
    def construct(self):
        #Plan pendant la création
        plane = NumberPlane()
        #self.add(plane)

        #Titre
        text1 = Text(r"La méthode d'Héron",font_size=85)
        text1.move_to([0,0,0])
        self.play(Write(text1,run_time=2))
        self.wait(3)

        self.play(ScaleInPlace(text1,0.5))
        self.play(text1.animate.move_to([0,3.4,0]))
        self.wait(2)

        #Racine
        text2 = MathTex(r"\sqrt(A)\space = \space ?",font_size=60)
        text2.move_to([-5,0,0])

        #Représantation rectangle
        rec1 = Rectangle(height=3.5,width=1)
        rec1.move_to([0,0,0])
        
        text3 = MathTex(r"x",font_size=43).next_to(rec1,DOWN)
        text4 = MathTex(r"y",font_size=43).next_to(rec1,LEFT)

        rec1_group=VGroup(
            rec1,
            text3,
            text4
        )

        #Représentation du carré
        square1 = Square(side_length=1.87)
        square1.move_to([5,0,0])

        text5 = VGroup(
            MathTex(r"c",font_size=43).next_to(square1,DOWN),
            MathTex(r"c",font_size=43).next_to(square1,RIGHT)
        )

        square1_group=VGroup(
            square1,
            text5
        )

        #Représentation de l'égalité
        text6 = VGroup(
            MathTex(r"Aire", font_size=44),
            MathTex(r"\longleftrightarrow", font_size=59)
        )
        text6[1].next_to(text6[0],DOWN)
        text6.move_to([2.5,0,0])

        #Racine
        self.play(Write(text2))
        self.wait(1)

        #2 Egalité
        self.play(Create(rec1,run_time=1.5),Create(square1,run_time=1.5,lag_ratio=0.5))
        self.play(FadeIn(text3,text4,text5))
        self.wait(0.2)
        self.play(Write(text6,run_time=1.5))
        self.play(ShowCreationThenFadeOut(rec1.copy().set_fill(color=ORANGE,opacity=0.8)),
                  ShowCreationThenFadeOut(square1.copy().set_fill(color=ORANGE,opacity=0.8)))

        #self.add(text2, rec1, text3, text4, square1, text5, text6)
        self.wait(2)

        #Transformation1 du Rectangle
        rec2 = Rectangle(width=1.5,height=35/15)
        rec2.move_to((0,0,0))

        rec2_group = VGroup(
            rec2,
            MathTex(r"x",font_size=43).next_to(rec2,DOWN),
            MathTex(r"y",font_size=43).next_to(rec2,LEFT)
        )
        self.play(Transform(rec1_group,rec2_group,run_time=2))
        self.play(ShowCreationThenFadeOut(rec2.copy().set_fill(color=ORANGE,opacity=0.8)),
                  ShowCreationThenFadeOut(square1.copy().set_fill(color=ORANGE,opacity=0.8)))

        #Transformation2 du Rectangle
        rec3 = Square(side_length=1.87)
        rec3.move_to((0,0,0))

        rec3_group = VGroup(
            rec3,
            MathTex(r"x",font_size=43).next_to(rec3,DOWN),
            MathTex(r"y",font_size=43).next_to(rec3,LEFT)
        )
        self.play(Transform(rec1_group,rec3_group,run_time=2))
        self.play(ShowCreationThenFadeOut(rec3.copy().set_fill(color=ORANGE,opacity=0.8)),
                  ShowCreationThenFadeOut(square1.copy().set_fill(color=ORANGE,opacity=0.8)))
        self.wait(1)

        #Disparition Ecran
        all_1 = VGroup(
            text2,
            text5,
            text6,
            square1,
            rec1_group
        )
        self.play(FadeOut(all_1,run_time=2))


        #-----------------------------------#


        #Example avec une Aire de 25 :
        text9 = MathTex(r"\sqrt(25)\space = \space ?",font_size=55)
        text9.move_to([-5,0,0])
        self.play(Write(text9))
        self.wait(2)
        """
        1 ; 25
        2 ; 12,5
        4 ; 6,25
        5 ; 5
        """
        steps=[[1,25],[2,12.5],[4,6.25],[5,5]]
        tour=0
        group_list=[]
        for step in steps:
            rec4 = Rectangle(width=step[0]*6/25,height=step[1]*6/25).move_to([0,0,0])
            accolade1 = Brace(rec4,DOWN,buff=0.1)
            accolade2 = Brace(rec4,RIGHT,buff=0.1)
            text7 = MathTex(f"{step[0]}", font_size=43).next_to(accolade1,DOWN).shift(0.15*UP)
            text8 = MathTex(f"{step[1]}", font_size=43).next_to(accolade2,RIGHT).shift(0.15*LEFT)
            text10 = MathTex(f"{step[0]}\space * \space {step[1]} = 25", font_size=55).move_to([4.8,0,0])
            rec4_group = VGroup(
                rec4,
                accolade1,
                accolade2,
                text7,
                text8,
                text10
            )
            if tour == 0:
                self.play(Create(rec4))
                self.play(FadeIn(accolade1))
                self.play(Write(text7))
                self.play(FadeIn(accolade2))
                self.play(Write(text8))
                self.wait(1)
                self.play(Write(text10))
            else:
                self.play(Transform(group_list[0],rec4_group))
            group_list.append(rec4_group)
            self.wait(1)
            tour+=1
        result_text_group = VGroup(
            text9,
            group_list[0][5]
        )
        result_text = MathTex(r"\sqrt{25} \space = \space 5").move_to([0,-3,0])
        self.play(Transform(result_text_group,result_text, run_time=1.34))

        self.wait(3)

        all_2 = VGroup(
            result_text_group,
            group_list[0]
        )
        self.play(FadeOut(all_2,run_time=2))
        self.wait(1)

        #-----------------------------------#

        #Apparition de la racine de 36
        text11 = MathTex(r"\sqrt{36} \space = \space ?", font_size=50).move_to([8,3,0]).rotate(-PI/9)
        self.play(text11.animate.move_to([5.5,3,0]))
        self.wait(1)

        #Etape1 : Définir 1 côté du rectangle
        text12 = Text("Etape 1 : définir 1 côté du rectangle", 
                      t2w={"Etape 1 :": BOLD},
                      t2c={"Etape 1 :":"#00FFFF"}, 
                      font_size=38).move_to([0,2.45,0])
        
        self.play(Write(text12,run_time=2))
        self.wait(1)

        rec5 = Rectangle(width=2*4/18, height=18*4/18).move_to([0,-0.2,0])
        accolade3 = Brace(rec5,DOWN,buff=0.1)
        text13 = MathTex(r"x \space = \space 2").next_to(accolade3,DOWN).shift(0.15*UP)

        self.play(Create(rec5))
        self.play(FadeIn(accolade3))
        self.play(Write(text13))

        self.wait(2)

        #Etape 2 : Calculer y en fonction de x
        text14 = Text("Etape 2 : Calculer y", 
                      t2w={"Etape 2 :": BOLD},
                      t2c={"Etape 2 :":"#00FFFF"}, 
                      font_size=38).move_to([0,2.45,0])
        
        self.play(Transform(text12,text14))
        
        accolade4 = Brace(rec5,RIGHT,buff=0.2)
        text15 = MathTex(r"y \space = \space ?", font_size=43).next_to(accolade4,RIGHT).shift(0.1*LEFT)

        self.play(FadeIn(accolade4))
        self.play(Write(text15))

        steps = [r"x \space * \space y \space = \space Aire",
                 r"y \space = \space \frac{Aire}{x}",
                 r"y \space = \space \frac{36}{2}",
                 r"y \space = \space 18"]
        tour = 0
        position = [5,1.4,0]
        old_txt=[]
        for step in steps:
            txt = MathTex(step,font_size=43).move_to(position)
            if tour == 0:
                old_txt.append(txt)
                self.play(Write(txt))
            else:
                ok=old_txt[-1].copy()
                self.play(Transform(ok,txt))
                old_txt.append(ok) 
            self.wait(1)
            position[1] = position[1] - 1.3
            tour+=1
        self.wait(0.3)

        surrounding1 = SurroundingRectangle(old_txt[-1], color=YELLOW,buff=0.15).rotate(PI)
        self.play(Create(surrounding1, run_time=0.7))

        text16 = MathTex(r"y \space = \space 18").next_to(accolade4,RIGHT).shift(0.1*LEFT)
        self.play(FadeOut(surrounding1),Transform(text15,text16))
        self.wait(2)

        txt_group = VGroup()
        for i in old_txt:
            print(i)
            txt_group.add(i)
        self.play(FadeOut(txt_group))
        self.wait(1)

        #Etape 3 : Transformation en carré
        text17 = Text("Etape 3 : Transformation en carré", 
                      t2w={"Etape 3 :": BOLD},
                      t2c={"Etape 3 :":"#00FFFF"}, 
                      font_size=38).move_to([0,2.45,0])
        rec5_group = VGroup(
            rec5,
            accolade3,
            accolade4,
            text13,
            text15
        )
        self.play(Transform(text12,text17),
                  rec5_group.animate.shift(3*LEFT))

        text18 = Text("Moyenne des côtés",
                      font_size=36,
                      color="#FF0000")
        text18.move_to([3.7,1.3,0])
        surrounding2 = SurroundingRectangle(text18, buff=0.2, color="#AF0000")
        text18_group = VGroup(
            text18,
            surrounding2,
        )
        self.play(FadeIn(text18_group))

        self.wait(1)

        text19 = MathTex(r"x'\space = \space \frac{x\space + \space y}{2}", font_size=43)
        text19.next_to(text18_group,DOWN).shift(0.3*DOWN)
        text20 = MathTex(r"x' \space = \space \frac{2+18}{2}", font_size=43)
        text20.next_to(text19,DOWN).shift(0.2*DOWN)
        text21 = MathTex(r"x' \space = \space 10", font_size=43)
        text21.next_to(text20,DOWN).shift(0.2*DOWN)
        
        self.play(Write(text19))
        self.wait(1)
        self.play(Write(text20))
        self.wait(1)
        self.play(Write(text21))

        surrounding4 = SurroundingRectangle(text21,YELLOW,buff=0.15)
        self.play(Create(surrounding4, run_time=0.5))

        self.wait(2)
        
        #Etape 4 : On recommence avec le nouveau x
        text22 = Text("Etape 4 : On recommence avec le nouveau x'", 
                      t2w={"Etape 4 :": BOLD},
                      t2c={"Etape 4 :":"#00FFFF"}, 
                      font_size=38).move_to([0,2.45,0])
        self.play(Transform(text12,text22))

        self.wait(1)

        tour=0
        oldrec_group=rec5_group
        x=10
        for i in range(5):
            rec6 = Rectangle(width=x*4/18, height=36/(x)*4/18)
            rec6.move_to([-3,-0.2,0])
            acc = VGroup(
                Brace(rec6, DOWN, buff=0.15),
                Brace(rec6, RIGHT, buff=0.15)
            )
            txt_rec6 = VGroup(
                MathTex(f"x \space = \space {round(x,2)}", font_size=43).next_to(acc[0],DOWN),
                MathTex(f"y \space = \space ?", font_size=43).next_to(acc[1],RIGHT),
                MathTex(f"y \space = \space {round(36/x,2)}", font_size=43).next_to(acc[1],RIGHT)
            )
            rec6_group1 = VGroup(
                rec6,
                acc,
                txt_rec6[0],
                txt_rec6[1]
            )
            rec6_group2 = VGroup(
                rec6,
                acc,
                txt_rec6[0],
                txt_rec6[2]
            )
            self.play(Transform(oldrec_group, rec6_group1))

            if True:
                surrounding5 = SurroundingRectangle(rec6_group1[2], YELLOW, buff=0.2)
                self.play(Create(surrounding5, run_time=0.5))
                self.wait(0.1)
                self.play(FadeOut(surrounding4),FadeOut(surrounding5))
                if tour == 0:
                    self.play(FadeOut(text18_group),FadeOut(text19),FadeOut(text20),FadeOut(text21))
                else :
                    self.play(FadeOut(text19),FadeOut(text20),FadeOut(text21))
                self.wait(0.3)
            
            #Calcul y:
            aire = '{36}'
            xx = '{' + str(round(x,2)) + '}'
            steps = [r"x \space * \space y \space = \space Aire",
                    r"y \space = \space \frac{Aire}{x}",
                    f"y \space = \space \\frac{aire}{xx}",
                    f"y \space = \space {round(36/x,2)}"]
            tour = 0
            position = [4,0.5,0]
            old_txt=[]
            for step in steps:
                txt = MathTex(step,font_size=43).move_to(position)
                if tour == 0:
                    old_txt.append(txt)
                    self.play(Write(txt))
                else:
                    ok=old_txt[-1].copy()
                    self.play(Transform(ok,txt))
                    old_txt.append(ok) 
                self.wait(1)
                position[1] = position[1] - 1.3
                tour+=1
            self.wait(0.3)
            
            surrounding3 = SurroundingRectangle(old_txt[-1],YELLOW,buff=0.15)
            self.play(Create(surrounding3))
            self.play(FadeOut(surrounding3))

            self.play(Transform(oldrec_group,rec6_group2))

            tt = VGroup()
            for t in old_txt:
                tt.add(t)
            self.play(FadeOut(tt))

            #Stop
            if round(36/x,2) == 6.0:
                print("STOPPP")
                break

            #Moyenne :
            numerateur = "{" + str(round(x,2)) + "\space + \space" + str(round(36/x,2)) + "}"
            denominateur = "{" + str(2) + "}"
            text19 = MathTex(r"x'\space = \space \frac{x\space + \space y}{2}", font_size=43)
            text19.move_to([4.2,0.5,0])
            text20 = MathTex(f"x' \space = \space \\frac{numerateur}{denominateur}", font_size=43)
            text20.next_to(text19,DOWN).shift(0.2*DOWN)
            text21 = MathTex(f"x' \space = \space {round((x+36/x)/2,2)}", font_size=43)
            text21.next_to(text20,DOWN).shift(0.2*DOWN)
            
            self.play(Write(text19))
            self.wait(0.3)
            self.play(Write(text20))
            self.wait(0.3)
            self.play(Write(text21))
            self.wait(0.3)

            surrounding4 = SurroundingRectangle(text21,YELLOW,buff=0.15)
            self.play(Create(surrounding4, run_time=0.5))

            x=(x+36/x)/2
            print("NEW X :",x)
            tour+=1
        
        self.play(oldrec_group.animate.move_to([-2.5,-1.3,0]))
        self.play(ScaleInPlace(oldrec_group,1.2))

        text23 = MathTex(r"\sqrt{36} = 6", font_size=65).move_to([2.5,-1.3,0])
        self.play(Write(text23,run_time=2))
        self.wait(3)

        all_3 = VGroup(
            oldrec_group,
            text23,
            text1,
            text11,
            text12
        )
        self.play(FadeOut(all_3,run_time=2))
        self.wait(2)



