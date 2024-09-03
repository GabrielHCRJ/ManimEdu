#FAZER A MESMA COISA MAS COM CINCO INTERVALOS

from manim import *
from numpy import *


class CosPeriodicidade(Scene):
    def construct(self):
        axes= Axes(x_range=[-7*pi/2,7*pi/2],y_range=[-3,3],x_length=12,y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axes_labels=axes.get_axis_labels(x_label="x",y_label="y")
        cosseno=MathTex("f(x)=cos(x)").set_color(RED).set_height(0.5).shift(2.5*UP,3*LEFT)
        texto=MathTex("Periodicidade:", font_size=36).shift(3.25*UP)
        texto2=Tex("A\ função cosseno\ se\ repete\ a\ cada\ intervalo\ de\ ", font_size=32)
        texto3=MathTex("2\pi", font_size=32).next_to(texto2,RIGHT, buff=0.2)
        grupo=VGroup(texto2,texto3).shift(3*DOWN)
        
        cosseno_azul=axes.plot(lambda x: cos(x),x_range=[-7*pi/2,7*pi/2], color=BLUE)

        graph00=axes.plot(lambda x: cos(x),x_range=[-7*pi/2,-3*pi/2], color=RED)
        graph0=axes.plot(lambda x: cos(x),x_range=[-3/2*pi,pi/2], color=RED)
        graph1=axes.plot(lambda x: cos(x),x_range=[pi/2,5*pi/2], color=RED)
       

        ponto0=Dot(axes.c2p(-5/2*pi,0),color=RED,fill_opacity=5,stroke_width=1)
        label0=MathTex("(-\\frac{5\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto0, DOWN + LEFT, buff=0.2)
       
        ponto1=Dot(axes.c2p(-3/2*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        label1=MathTex("(-\\frac{3\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto1, DOWN + LEFT, buff=0.2)

        ponto2=Dot(axes.c2p(-pi/2,0), color=RED, fill_opacity=5,stroke_width=1)
        label2=MathTex("(-\\frac{\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto2, DOWN+LEFT, buff=0.2)

        ponto3=Dot(axes.c2p(pi/2,0), color=RED, fill_opacity=5, stroke_width=1)
        label3=MathTex("(\\frac{\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto3, DOWN+RIGHT, buff=0.2)

        ponto4=Dot(axes.c2p(3*pi/2,0), color=RED, fill_opacity=5, stroke_width=1)
        label4=MathTex("(\\frac{3\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto4, DOWN+RIGHT, buff=0.2)

        ponto5=Dot(axes.c2p(5*pi/2,0), color=RED, fill_opacity=5, stroke_width=1)
        label5=MathTex("(\\frac{5\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto5, DOWN+RIGHT, buff=0.2)

        
        
        line0 = DashedLine(start=axes.c2p(-3*pi/2,-3),end=axes.c2p(-3/2*pi,2.5))
        line1 = DashedLine(start=axes.c2p(pi/2,-3),end=axes.c2p(pi/2,3))
        line2 = DashedLine(start=axes.c2p(5/2*pi,-3),end=axes.c2p(5/2*pi,3))
       
        linhas=VGroup(line0,line1,ponto0,label0,ponto1,label1,ponto4,label4,ponto5,label5)


        self.play(DrawBorderThenFill(axes))
        self.play(Write(axes_labels))
        self.play(Write(cosseno))
        self.play(Write(texto))
        self.play(Create(cosseno_azul),run_time=2)
        self.play(Create(graph00))
        self.play(Create(ponto0),Write(label0))
        self.play(Create(graph0))
        self.play(Create(ponto1),Write(label1))
        self.play(Create(graph1))
        self.play(Create(ponto2),Write(label2))
     
        self.play(Create(ponto3),Write(label3))
    
        self.play(Create(ponto4),Write(label4))

        self.play(Create(ponto5),Write(label5))

        
        self.play(Create(line0))
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(FadeOut(cosseno_azul))
        self.wait(2)#aqui que começam as edições#
        self.play(FadeOut(line2)) 
        self.wait()   
        self.play(Transform(graph00,graph0),Transform(graph1,graph0),run_time=5)
        self.wait(2)
        self.play(Write(grupo))
       
        self.wait(4)