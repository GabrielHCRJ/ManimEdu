from manim import *
from numpy import *

class TgReciproca(Scene):
    def construct(self):
        axes = Axes(x_range=[-3*pi,3*pi], x_length=10, y_range=[-10,10], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axes2 = Axes(x_range=[-3*pi,3*pi], x_length=10, y_range=[-10,10], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")

        #TG
        tg1 = axes.plot((lambda x: tan(x)), x_range=[-3*pi,(-5*pi/2)-0.10], color=RED, stroke_width=5)
        tg2 = axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,(-3*pi/2)-0.10], color=RED, stroke_width=5)
        tg3 = axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,(-pi/2)-0.10], color=RED, stroke_width=5)
        tg4 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        tg5 = axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,((3*pi)/2)-0.10], color=RED, stroke_width=5)
        tg6 = axes.plot((lambda x: tan(x)), x_range=[(3*pi/2)+0.10,(5*pi/2)-0.10], color=RED, stroke_width=5)
        tg7 = axes.plot((lambda x: tan(x)), x_range=[(5*pi/2)+0.10,3*pi], color=RED, stroke_width=5)

               
       
        #graficos do cotg

        graph = axes2.plot(lambda x: 1/tan(x), x_range=[-3*pi+0.10,-2*pi-0.10], color=RED)
        graph2 = axes2.plot(lambda x: 1/tan(x), x_range=[-2*pi+0.10,-pi-0.10], color=RED)
        graph3 = axes2.plot(lambda x:1/tan(x), x_range=[-pi+0.10,-0.10], color=RED)
        graph4 = axes2.plot(lambda x:1/tan(x), x_range=[+0.10,pi-0.10], color=RED)
        graph5 = axes2.plot(lambda x: 1/tan(x), x_range=[pi+0.10,2*pi-0.10], color=RED)
        graph6 = axes2.plot(lambda x: 1/tan(x), x_range=[2*pi+0.10,3*pi-0.10], color=RED)
      
        #TEXTOS#

        reciproca=MathTex("Reciproca:", font_size=36, color=WHITE).shift(3.25*UP)
        tangente=MathTex("f(x)=tg(x)", font_size=36, color=RED).shift(3.25*UP+3*LEFT)
        tangente_copy=tangente.copy()
        cotg=MathTex("g(x)=\\frac{1}{f(x)}=cotg(x)", font_size=36, color=RED).shift(3.25*UP+3.25*RIGHT)
        
        self.play(Create(axes),Create(axes_label))
        self.play(Write(reciproca),run_time=2)
    
        self.play(Write(tangente),Write(tangente_copy))
        self.play(Create(tg1))
        self.play(Create(tg2))
        self.play(Create(tg3))
        self.play(Create(tg4))
        self.play(Create(tg5))
        self.play(Create(tg6))
        self.play(Create(tg7))            
        
        self.play(Transform(tangente, cotg),run_time=3)

        self.play(Transform(tg1,graph),run_time=3)
        self.play(Transform(tg2,graph2),run_time=3)
        self.play(Transform(tg3,graph3,run_time=3))
        self.play(Transform(tg4,graph4),run_time=3)
        self.play(Transform(tg5,graph5),run_time=3)
        self.play(Transform(tg6,graph6),FadeOut(tg7),run_time=3)

        
        
        self.wait(5)
        
        