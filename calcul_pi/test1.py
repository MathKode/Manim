from manim import *
import math

#python3.exe -m manim -pql test1.py Animation

class Animation(MovingCameraScene):
    def construct(self):
        plane = NumberPlane()
        #self.add(plane)

        text1 = Text(r'Comment calculer le nombre Pi ?',font_size=43)
        self.play(Write(text1))
        self.wait(2)
        self.play(text1.animate.move_to([0,3,0]))
        self.wait(2)

        #Line
        d1=Dot([-1.5,0,0])
        d3=Dot([1.5,0,0])
        ligne = Line([-1.5,0,0],[1.5,0,0], color=WHITE)
        txt = Text(r'd = 1',font_size=28).next_to(ligne, UP)
        self.play(FadeIn(d1,run_tim=0.5),FadeIn(d3,run_tim=0.5))
        self.play(Create(ligne, run_time=1.2))
        self.play(Write(txt))
        self.wait(1)

        d2=Dot([0,0,0])
        ligne2 = Line([0,0,0],[1.5,0,0], color=WHITE)
        txt2 = Text(r'r = 1/2', font_size=26).next_to(ligne, UP)
        self.play(Transform(ligne,ligne2), Transform(txt, txt2), FadeIn(d2,run_time=0.5),FadeOut(d1,run_time=0.5))
        self.wait(1)
        circle1 = Circle(radius=1.5, color=WHITE)
        self.play(Create(circle1), FadeOut(d3))
        self.wait(2)
        
        nb_cote = 4
        for i in range(3):
            if i!=0:
                self.play(FadeOut(poly))
            a = 360/nb_cote #angle deg
            dot_list = []
            ang=0
            for p in range(0,nb_cote,1):
                print(ang)
                y = math.sin(ang*math.pi/180) * 1.5
                x = math.cos(ang*math.pi/180) * 1.5
                dot_list.append([x,y,0])
                ang+=a
            print("DOT LIST :", dot_list)
            poly = Polygon(*dot_list, color=ORANGE)
            self.play(Create(poly, run_time=2))
            self.wait(1)
            nb_cote=nb_cote*2
        #ZOOM
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=circle1.height*0.5).move_to(circle1).shift(RIGHT*1.25+UP*0.25))
        self.wait(1)
        #Continue la création de coté
        for i in range(3):
            self.play(FadeOut(poly, run_time=0.5))
            a = 360/nb_cote #angle deg
            dot_list = []
            ang=0
            for p in range(0,nb_cote,1):
                print(ang)
                y = math.sin(ang*math.pi/180) * 1.5
                x = math.cos(ang*math.pi/180) * 1.5
                dot_list.append([x,y,0])
                ang+=a
            print("DOT LIST :", dot_list)
            poly = Polygon(*dot_list, color=ORANGE)
            self.play(Create(poly, run_time=0.5))
            nb_cote=nb_cote*2
            self.wait(0.2)
        #Restore Scene
        self.play(Restore(self.camera.frame))
        self.wait(1)
        
        #A SUPP
        #poly=Polygon(*[[1.5,0,0],[0,1.5,0],[-1.5,0,0],[0,-1.5,0]], color=ORANGE)
        #self.add(poly)
        ####
        txt3 = Text(r'-> Périmètre = Pi', font_size=40 ,color=ORANGE).next_to(poly,RIGHT)
        self.play(Create(txt3))
        self.wait(2)
        self.play(FadeOut(poly), FadeOut(txt3))

        #Les Calculs

        #Structure
        nb_cote = 8
        a = 360/nb_cote #angle deg
        dot_list = []
        ang=0
        for p in range(0,nb_cote,1):
            print(ang)
            y = math.sin(ang*math.pi/180) * 1.5
            x = math.cos(ang*math.pi/180) * 1.5
            dot_list.append([x,y,0])
            ang+=a
        print("DOT LIST :", dot_list)
        poly = Polygon(*dot_list, color=ORANGE)
        self.play(Create(poly, run_time=1))

        self.wait(2)

        txt4 = Text('c',font_size=25,color=ORANGE).move_to([1.55,0.6,0])
        txt55 = Text('Périmètre = 8*c ≈ Pi', font_size=35, color=ORANGE).move_to([4.25,1.7,0])
        self.play(FadeIn(txt4))
        self.wait(1)
        self.play(FadeIn(txt55))
        self.wait(2)

        
        #Triangle :
        l1 = Line(*[dot_list[1],[0,0,0]],color=BLUE)
        l2 = Line(*[[0,0,0],dot_list[0]],color=BLUE)
        base_tr=Line(*[dot_list[0],dot_list[1]], color=ORANGE)
        info1 = Text(r'\\', font_size=12, color=BLUE)
        info2 = Text(r'\\', font_size=12, color=BLUE)
        info1.move_to([0.53,0.53,0])
        info2.move_to([0.75,0,0])
        self.play(Create(l1, run_time=1))
        self.play(Create(l2, run_time=1), txt.animate.shift(0.75*DOWN+0.2*RIGHT))
        self.add(base_tr)
        self.play(FadeIn(info1), FadeIn(info2))
        self.wait(2)

        groupe_triangle_or = VGroup(
            l1,
            l2,
            base_tr,
            info1,
            info2
        )

        groupe_fig = VGroup(
            circle1,
            poly,
            groupe_triangle_or,
            d2,
            txt,
            txt4,
            ligne2
        )
        groupe_triangle = groupe_triangle_or.copy()
        self.play(groupe_triangle.animate.move_to([2.75,-0.4,0]),
                  groupe_fig.animate.move_to([-3,0,0]))
        self.play(Rotate(groupe_triangle, angle=-56/90*PI))
        self.play(ScaleInPlace(groupe_triangle,1.3))
        self.wait(1)

        txt5 = Text('c = ?',font_size=25,color=ORANGE).next_to(groupe_triangle, DOWN)
        txt6 = Text('r = 1/2',font_size=25,color=BLUE).next_to(groupe_triangle, RIGHT)
        txt7 = Text('a = 360/8 = 45°',font_size=25,color=YELLOW).next_to(groupe_triangle, UP).shift(0.4*RIGHT+0.1*DOWN)


        point1 = groupe_triangle[1].get_projection([2.5,0,0])
        point2 = groupe_triangle[0].get_projection([2.7,0,0])
        print("POINT1 POINT2 :",point1,point2)
        ang = ArcBetweenPoints(start=point1,end=point2,stroke_color=YELLOW)

        self.play(Write(txt5))
        self.wait(0.5)
        self.play(Write(txt6))
        self.wait(0.5)
        self.play(Create(ang))
        self.play(Write(txt7,run_time=2))
        self.wait(3)

        mediatrice = Line(*[[2.57,0.69,0],[2.57,-1.1,0]],color=WHITE)
        point1_ = groupe_triangle[2].get_projection([2.8,0,0])
        point3_ = [2.57,-0.91,0]
        point2_ = [point1_[0], point3_[1],0]


        ll1 = Line(point1_,point2_,color=WHITE)
        ll2 = Line(point2_,point3_,color=WHITE)
        self.play(Create(mediatrice))
        self.play(Create(ll1))
        self.play(Create(ll2))
        self.wait(2)

        e1 = Text("D'après le Théorème de Pythagore, on a :", font_size=30, color=WHITE).next_to(txt5, DOWN*1.3)
        e2 = Text("sin(a/2)=(1/2*c)/r=(1/2*c)/(1/2)=c", font_size=30, color=WHITE).next_to(e1, DOWN)
        
        self.play(Write(e1, run_time=2.5))
        self.play(Write(e2, run_time=2.5))
        self.wait(1)
        txt5_ = Text('c = sin(a/2)',font_size=25,color=ORANGE).next_to(groupe_triangle, DOWN)
        self.play(Transform(txt5, txt5_))
        self.wait(4)

        supp = VGroup(
            groupe_triangle,
            txt5,
            txt6,
            txt7,
            e1,
            e2,
            ang,
            mediatrice,
            ll1,
            ll2
        )
        self.play(FadeOut(supp,run_time=2))
        self.wait(1)

        p1 = Text("c = sin(a/2)", font_size=30).next_to(txt55,1.5*DOWN)
        p2 = Text("a = 360/Nombre Coté", font_size=30).next_to(p1,DOWN)
        p3 = Text("Pour n nombre de coté, entier>3 ,  on a :", font_size=30).next_to(p2,1.5*DOWN)
        p4 = Text("Un = n * sin(360/2n)", font_size=30).next_to(p3,1.5*DOWN)

        self.play(Write(p1, run_time=1.5))
        self.wait(1)
        self.play(Write(p2, run_time=1.5))
        self.wait(1)
        self.play(Write(p3, run_time=1.5))
        self.wait(1)
        self.play(Write(p4, run_time=1.5))
        self.wait(5)

        self.clear()




        
        



        





        