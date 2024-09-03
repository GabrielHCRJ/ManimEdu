from manim import *
from numpy import *
class TgSimetria(Scene):
    def construct(self):
        
        axes = Axes(x_range=[-3*pi,3*pi],x_length=10,y_range=[-10,10], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")

        

        tg1 = axes.plot((lambda x: tan(x)), x_range=[-3*pi,(-5*pi/2)-0.10], color=RED, stroke_width=5)
        tg2 = axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,(-3*pi/2)-0.10], color=RED, stroke_width=5)
        tg3 = axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,(-pi/2)-0.10], color=RED, stroke_width=5)
        tg4 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        tg41 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        tg5 = axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,((3*pi)/2)-0.10], color=RED, stroke_width=5)
        tg6 = axes.plot((lambda x: tan(x)), x_range=[(3*pi/2)+0.10,(5*pi/2)-0.10], color=RED, stroke_width=5)
        tg7 = axes.plot((lambda x: tan(x)), x_range=[(5*pi/2)+0.10,3*pi], color=RED, stroke_width=5)
        simetria=MathTex("Simetria:",font_size=36).shift(3.25*UP)

       

        x=ValueTracker(1)
        #TESTE
        angle = 180*DEGREES

        r=ValueTracker(1)
        ponto1=Dot(axes.c2p(1,pi/2), color=RED)
        ponto2=Dot(axes.c2p(-1,-pi/2), color=RED)
      

        line1 = DashedLine(start=axes.c2p(1,0),end=axes.c2p(1,pi/2))
        line2 = DashedLine(start=axes.c2p(0,pi/2),end=axes.c2p(1,pi/2))

        line3 = DashedLine(start=axes.c2p(-1,0),end=axes.c2p(-1,-pi/2))
        line4 = DashedLine(start=axes.c2p(0,-pi/2),end=axes.c2p(-1,-pi/2))

        label1=MathTex("(x,tg(x))", color=WHITE, font_size=20).next_to(ponto1, UP + RIGHT, buff=0.2)
        label2=MathTex("(-x,-tg(x))", color=WHITE, font_size=20).next_to(ponto2, DOWN + LEFT, buff=0.2)
       
        
     #

        resposta=Text("Função Ímpar:",font_size=22).shift(3*RIGHT+2.5*UP)
        resposta2=Text("Simétrica em relação à origem ",font_size=22).shift(3*RIGHT+2*UP)
        resposta3=MathTex("tg(-x)=-tg(x)",font_size=26).shift(3*RIGHT+1.5*UP)
        tg=MathTex("f(x)=tg(x)",font_size=28,color=RED).shift(2.5*UP+2.5*LEFT).set_height(0.5)
        
        
        self.play(Create(axes),Write(axis_labels),run_time=2)
        self.play(Create(simetria))
        self.wait()
        self.play(Write(tg))

        self.play(Create(tg1))
        self.play(Create(tg2))
        self.play(Create(tg3))
        self.play(Create(tg4),Create(tg41))
        self.play(Create(tg5))
        self.play(Create(tg6))
        self.play(Create(tg7))
        self.wait()
        self.play(FadeOut(tg1),FadeOut(tg2),FadeOut(tg3),FadeOut(tg5),FadeOut(tg6),FadeOut(tg7),)


        self.play(Create(line1),Create(line2))
        self.play(Create(ponto1))        
        self.play(Write(label1))

        self.play(Create(ponto2))
        
        self.wait()
        self.play(FadeOut(line1),FadeOut(line2),FadeOut(label1))


        self.play(Rotate(tg4,angle),run_time=4)
        
        self.play(Create(line3),Create(line4))
        self.play(Create(label2))

        
        self.wait(1)
        self.play(FadeOut(line3),FadeOut(line4),FadeOut(label2))
        
        
        
        self.wait()
        self.play(Create(resposta))
        self.play(Create(resposta2))
        self.play(Create(resposta3))
        self.wait(4)