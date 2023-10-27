from manim import *
import math

#python3.exe -m manim -pql test2.py Animation

class Animation(MovingCameraScene):
    def construct(self):
        plane = NumberPlane()
        #self.add(plane)

        def Un(n):
           return str(round(n*math.sin(360*math.pi/180/(2*n)),5))
        
        text1 = Text(r'Un = n * sin(360/2n)',font_size=43).move_to([0,3,0])
        self.play(Write(text1))
        t0 = Table(
            [["N", "Un"],
            ["3", Un(3)]])
        self.play(Create(t0))
        self.wait(1)
        for i in range(4,100):
            tn = Table(
                [["N", "Un"],
                [str(i), Un(i)]])
            self.play(Transform(t0,tn,run_time=0.1))
        self.wait(2)
            
        
       

