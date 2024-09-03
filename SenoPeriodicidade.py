
from manim import *
from numpy import *


class SenoPeriodicidade(Scene):
    def construct(self):
        axes = Axes(x_range=[-10,10],x_length=10,y_range=[-3,3], y_length=5, axis_config={'include_tip':True}).set_color('BLUE')
        axes_labels=axes.get_axis_labels(x_label="x",y_label="y")
        seno=MathTex("f(x)=sen(x)").set_color(RED).set_height(0.5).shift(2.5*UP,3*LEFT)
        texto=MathTex("Periodicidade:", font_size=36).shift(3.25*UP)
        texto2=Tex("A\ função seno\ se\ repete\ a\ cada\ intervalo\ de\ ", font_size=32)
        texto3=MathTex("2\pi", font_size=32).next_to(texto2,RIGHT, buff=0.2)
        grupo=VGroup(texto2,texto3).shift(3*DOWN)
        
        seno_azul=axes.plot(lambda x: sin(x),x_range=[-6*pi,6*pi], color=BLUE)

        graph00=axes.plot(lambda x: sin(x),x_range=[-6*pi,-5*pi], color=RED)

        graph0=axes.plot(lambda x: sin(x),x_range=[-5*pi,-3*pi], color=RED)
        graph1=axes.plot(lambda x: sin(x),x_range=[-3*pi,-pi], color=RED)
        graph2=axes.plot(lambda x: sin(x),x_range=[-pi,pi], color = RED)
        graph3=axes.plot(lambda x: sin(x),x_range=[pi,3*pi], color = RED)
        graph4=axes.plot(lambda x: sin(x),x_range=[3*pi,5*pi], color=RED)
        graph5=axes.plot(lambda x: sin(x),x_range=[5*pi,6*pi], color=RED)
        


        ponto0=Dot(axes.c2p(-5*pi,0),color=RED,fill_opacity=5,stroke_width=1)
        label0=MathTex("(-5\pi,0)", color=WHITE, font_size=20).next_to(ponto0, DOWN + LEFT, buff=0.2)
       
        ponto1=Dot(axes.c2p(-3*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        label1=MathTex("(-3\pi,0)", color=WHITE, font_size=20).next_to(ponto1, DOWN + LEFT, buff=0.2)

        ponto2=Dot(axes.c2p(-pi,0), color=RED, fill_opacity=5,stroke_width=1)
        label2=MathTex("(-\pi,0)", color=WHITE, font_size=20).next_to(ponto2, DOWN+LEFT, buff=0.2)

        ponto3=Dot(axes.c2p(pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label3=MathTex("(\pi,0)", color=WHITE, font_size=20).next_to(ponto3, DOWN+RIGHT, buff=0.2)

        ponto4=Dot(axes.c2p(3*pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label4=MathTex("(3\pi,0)", color=WHITE, font_size=20).next_to(ponto4, DOWN+RIGHT, buff=0.2)

        ponto5=Dot(axes.c2p(5*pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label5=MathTex("(5\pi,0)", color=WHITE, font_size=20).next_to(ponto5, DOWN+RIGHT, buff=0.2)


        
        
        line0 = DashedLine(start=axes.c2p(-5*pi,-3),end=axes.c2p(-5*pi,3))
        line1 = DashedLine(start=axes.c2p(-3*pi,-3),end=axes.c2p(-3*pi,2.5))
        line2 = DashedLine(start=axes.c2p(-pi,-3),end=axes.c2p(-pi,3))
        line3 = DashedLine(start=axes.c2p(pi,-3),end=axes.c2p(pi,3))
        line4 = DashedLine(start=axes.c2p(3*pi,-3),end=axes.c2p(3*pi,3))
        line5 = DashedLine(start=axes.c2p(5*pi,-3),end=axes.c2p(5*pi,3))
        
        linhas=VGroup(line0,line1,line4,line5,ponto0,label0,ponto1,label1,ponto4,label4,ponto5,label5)


        self.play(DrawBorderThenFill(axes))
        self.play(Write(axes_labels))
        self.play(Write(seno))
        self.play(Write(texto))
        self.play(Create(seno_azul),run_time=2)
        self.play(Create(graph00),run_time=2)
        self.play(Create(ponto0),Write(label0))
        self.play(Create(graph0),run_time=2)
        self.play(Create(ponto1),Write(label1))
        self.play(Create(graph1,run_time=2))
        self.play(Create(ponto2),Write(label2))
        self.play(Create(graph2),run_time=2)
        self.play(Create(ponto3),Write(label3))
        self.play(Create(graph3),run_time=2)
        self.play(Create(ponto4),Write(label4))
        self.play(Create(graph4),run_time=2)
        self.play(Create(ponto5),Write(label5))
        self.play(Create(graph5),run_time=2)
        
        self.play(Create(line0))
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Create(line3))
        self.play(Create(line4))
        self.play(Create(line5))

        self.wait(2)#aqui que começam as edições#
        self.play(FadeOut(linhas)) 
        self.wait()   
        self.play(FadeOut(graph00),FadeOut(graph5),FadeOut(graph0),Transform(graph0.copy(),graph2),FadeOut(graph1),Transform(graph1.copy(),graph2),FadeOut(graph3),Transform(graph3.copy(),graph2),FadeOut(graph4),Transform(graph4.copy(),graph2),run_time=3)
        self.wait(2)
        self.play(Write(grupo))
        self.play(Transform(graph2.copy(),graph1),
                  Transform(graph2.copy(),graph3),
                    FadeIn(ponto1),FadeIn(label1),FadeIn(ponto4),FadeIn(label4),
                    run_time=2)
 
        self.play(Transform(graph1.copy(),graph0),
                  Transform(graph3.copy(),graph4),
                  FadeIn(ponto0),FadeIn(label0),FadeIn(ponto5),FadeIn(label5),
                  run_time=2)

        self.play(FadeIn(graph00),FadeIn(graph5))

        self.wait(4)