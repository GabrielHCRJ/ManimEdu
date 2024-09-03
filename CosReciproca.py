from manim import *
from numpy import *

class CosReciproca(Scene):
    def construct(self):
        axes = Axes(x_range=[-7/2*pi,7/2*pi], x_length=10, y_range=[-5,5],y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axes2 = Axes(x_range=[-7/2*pi,7/2*pi], x_length=10, y_range=[-10,10],y_length=5)
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")

        cossenao= axes.plot(lambda x: cos(x),x_range=[-7/2*pi,7/2*pi],color=YELLOW )

        #SENAO nos intervalos do cossecante
        cosseno1=axes.plot(lambda x: cos(x),x_range=[-7/2*pi,-5/2*pi],color=YELLOW )
        cosseno2=axes.plot(lambda x: cos(x),x_range=[-5/2*pi,-3/2*pi], color=YELLOW )
        cosseno3=axes.plot(lambda x: cos(x),x_range=[-3/2*pi,-pi/2], color=YELLOW )
        cosseno4=axes.plot(lambda x: cos(x),x_range=[-pi/2,pi/2], color=YELLOW )
        cosseno5=axes.plot(lambda x: cos(x),x_range=[pi/2,3/2*pi], color=YELLOW )
        cosseno6=axes.plot(lambda x: cos(x),x_range=[3*pi/2,5/2*pi], color=YELLOW )
        cosseno7=axes.plot(lambda x: cos(x),x_range=[5/2*pi,7/2*pi], color=YELLOW )
       
        
       
        #graficos do secante

        graph = axes2.plot(lambda x: 1/cos(x), x_range=[-7/2*pi+0.10,-5/2*pi-0.10], color=RED)
        graph2 = axes2.plot(lambda x: 1/cos(x), x_range=[-5/2*pi+0.10,-3/2*pi-0.10], color=RED)
        graph3 = axes2.plot(lambda x:1/cos(x), x_range=[-3/2*pi+0.10,-pi/2-0.10], color=RED)
        graph4 = axes2.plot(lambda x:1/cos(x), x_range=[-pi/2+0.10,pi/2-0.10], color=RED)
        graph5 = axes2.plot(lambda x: 1/cos(x), x_range=[pi/2+0.10,3/2*pi-0.10], color=RED)
        graph6 = axes2.plot(lambda x: 1/cos(x), x_range=[3/2*pi+0.10,5/2*pi-0.10], color=RED)
        graph7 = axes2.plot(lambda x: 1/cos(x), x_range=[5/2*pi+0.10,7/2*pi-0.10], color=RED)
     
        #TEXTOS#

        reciproca=MathTex("Reciproca:", font_size=36, color=WHITE).shift(3.25*UP)
        cosseno=MathTex("f(x)=cos(x)", font_size=36, color=YELLOW).shift(3.25*UP+3*LEFT)
        cosseno_copy=cosseno.copy()
        sec=MathTex("g(x)=\\frac{1}{f(x)}=sec(x)", font_size=36, color=RED).shift(3.25*UP+3.25*RIGHT)
        
        self.play(Create(axes),Create(axes_label))
        self.play(Write(reciproca),run_time=2)
    
        self.play(Write(cosseno),Write(cosseno_copy))
        self.play(Create(cossenao), run_time=6)
        self.play(Create(cosseno1),Create(cosseno2),Create(cosseno3),Create(cosseno4),Create(cosseno5),Create(cosseno6),Create(cosseno7),run_time=1)        
        self.play(FadeOut(cossenao),run_time=3)

        self.play(Transform(cosseno, sec),run_time=1)

        self.play(Transform(cosseno1,graph),run_time=1)
        self.play(Transform(cosseno2,graph2),run_time=1)
        self.play(Transform(cosseno3,graph3,run_time=1))
        self.play(Transform(cosseno4,graph4),run_time=1)
        self.play(Transform(cosseno5,graph5),run_time=1)
        self.play(Transform(cosseno6,graph6),run_time=1)
        self.play(Transform(cosseno7,graph7),run_time=1)

        

        
        self.wait(6)
        
        