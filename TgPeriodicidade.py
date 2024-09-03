#FAZER A MESMA COISA MAS COM CINCO INTERVALOS

from manim import *
from numpy import *


class TgPeriodicidade(Scene):
    def construct(self):
        axes = Axes(x_range=[-3*pi,3*pi],x_length=10,y_range=[-10,10], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')           
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")

        tangente=MathTex("f(x)=tg(x)").set_color(RED).set_height(0.5).shift(2.5*UP,3*LEFT)
        texto=MathTex("Periodicidade:", font_size=36).shift(3.25*UP)
        texto2=Tex("A\ função seno\ se\ repete\ a\ cada\ intervalo\ de\ ", font_size=32)
        texto3=MathTex("2\pi", font_size=32).next_to(texto2,RIGHT, buff=0.2)
        grupo=VGroup(texto2,texto3).shift(3*DOWN)
               
                           
        graph00 = axes.plot((lambda x: tan(x)), x_range=[-3*pi,(-5*pi/2)-0.10], color=RED, stroke_width=5)
        graph0 = axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,(-3*pi/2)-0.10], color=RED, stroke_width=5)
        graph1 = axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,(-pi/2)-0.10], color=RED, stroke_width=5)
        graph2 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        graph3 = axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,((3*pi)/2)-0.10], color=RED, stroke_width=5)
        graph4 = axes.plot((lambda x: tan(x)), x_range=[(3*pi/2)+0.10,(5*pi/2)-0.10], color=RED, stroke_width=5)
        graph5 = axes.plot((lambda x: tan(x)), x_range=[(5*pi/2)+0.10,3*pi], color=RED, stroke_width=5)

        
        
       
        ponto2=Dot(axes.c2p(-pi/2,0), color=RED, fill_opacity=5,stroke_width=1)
        label2=MathTex("(\\frac{-\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto2, DOWN+LEFT, buff=0.2)

        ponto3=Dot(axes.c2p(pi/2,0), color=RED, fill_opacity=5, stroke_width=1)
        label3=MathTex("(\\frac{\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto3, DOWN+RIGHT, buff=0.2)

           
        
        
        line2 = DashedLine(start=axes.c2p(-pi/2,-10),end=axes.c2p(-pi/2,10))
        line3 = DashedLine(start=axes.c2p(pi/2,-10),end=axes.c2p(pi/2,10))
       
      
        self.play(DrawBorderThenFill(axes))
        self.play(Write(axis_labels))
        self.play(Write(tangente))
        self.play(Write(texto))
        
        self.play(Create(graph00))
        self.play(Create(graph0))
        
        self.play(Create(graph1))
        
        self.play(Create(graph2))
        
        self.play(Create(graph3))
        
        self.play(Create(graph4))
    
        self.play(Create(graph5))
        self.play(Create(ponto2),Write(label2))
        self.play(Create(ponto3),Write(label3))
        #self.play(Create(ponto2))
        #self.play(Create(ponto3))
        
        self.play(Create(line2))
        self.play(Create(line3))
   

        self.wait(2)#aqui que começam as edições#
        
        self.wait()   
        self.play(FadeOut(graph00),FadeOut(graph5),FadeOut(graph0),Transform(graph0.copy(),graph2),FadeOut(graph1),Transform(graph1.copy(),graph2),FadeOut(graph3),Transform(graph3.copy(),graph2),FadeOut(graph4),Transform(graph4.copy(),graph2),run_time=3)
        self.wait(2)
        self.play(Write(grupo))
        self.play(Transform(graph2.copy(),graph1),
                  Transform(graph2.copy(),graph3),
                                       run_time=2)
 
        self.play(Transform(graph1.copy(),graph0),
                  Transform(graph3.copy(),graph4),
                  
                  run_time=2)

        self.play(FadeIn(graph00),FadeIn(graph5))

        self.wait(4)