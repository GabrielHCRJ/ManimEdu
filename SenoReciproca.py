from manim import *
from numpy import *

class SenoReciproca(Scene):
    def construct(self):
        axes = Axes(x_range=[-3*pi,3*pi], x_length=10, y_range=[-5,5],y_length=5, axis_config={'include_tip':True}).set_color('BLUE')
        axes2 = Axes(x_range=[-3*pi,3*pi], x_length=10, y_range=[-10,10],y_length=5, axis_config={'include_tip':True}).set_color('BLUE')
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")

        senao= axes.plot(lambda x: sin(x),x_range=[-3*pi,3*pi],color=YELLOW )

        #SENAO nos intervalos do cossecante
        seno1=axes.plot(lambda x: sin(x),x_range=[-3*pi,-2*pi],color=YELLOW )
        seno2=axes.plot(lambda x: sin(x),x_range=[-2*pi,-pi], color=YELLOW )
        seno3=axes.plot(lambda x: sin(x),x_range=[-pi,0], color=YELLOW )
        seno4=axes.plot(lambda x: sin(x),x_range=[0,pi], color=YELLOW )
        seno5=axes.plot(lambda x: sin(x),x_range=[pi,2*pi], color=YELLOW )
        seno6=axes.plot(lambda x: sin(x),x_range=[2*pi,3*pi], color=YELLOW )
        
       
        #graficos do cossecante

        graph = axes2.plot(lambda x: 1/sin(x), x_range=[-3*pi+0.10,-2*pi-0.10], color=RED)
        graph2 = axes2.plot(lambda x: 1/sin(x), x_range=[-2*pi+0.10,-pi-0.10], color=RED)
        graph3 = axes2.plot(lambda x:1/sin(x), x_range=[-pi+0.10,-0.10], color=RED)
        graph4 = axes2.plot(lambda x:1/sin(x), x_range=[+0.10,pi-0.10], color=RED)
        graph5 = axes2.plot(lambda x: 1/sin(x), x_range=[pi+0.10,2*pi-0.10], color=RED)
        graph6 = axes2.plot(lambda x: 1/sin(x), x_range=[2*pi+0.10,3*pi-0.10], color=RED)
     
        #TEXTOS#

        reciproca=MathTex("Reciproca:", font_size=36, color=WHITE).shift(3.25*UP)
        seno=MathTex("f(x)=sen(x)", font_size=36, color=YELLOW).shift(3.25*UP+3*LEFT)
        seno_copy=seno.copy()
        cossec=MathTex("g(x)=\\frac{1}{f(x)}=cossec(x)", font_size=36, color=RED).shift(3.25*UP+3.25*RIGHT)
        
        self.play(Create(axes),Create(axes_label))
        self.play(Write(reciproca),run_time=2)
    
        self.play(Write(seno),Write(seno_copy))
        self.play(Create(senao), run_time=6)
        self.play(Create(seno1),Create(seno2),Create(seno3),Create(seno4),Create(seno5),Create(seno6),run_time=1)        
        self.play(FadeOut(senao),run_time=3)

        self.play(Transform(seno, cossec),run_time=3)

        self.play(Transform(seno1,graph),run_time=3)
        self.play(Transform(seno2,graph2),run_time=3)
        self.play(Transform(seno3,graph3,run_time=3))
        self.play(Transform(seno4,graph4),run_time=3)
        self.play(Transform(seno5,graph5),run_time=3)
        self.play(Transform(seno6,graph6),run_time=3)

        

        
        self.wait(6)
        
        