from manim import *
from numpy import *

class SenoConcavidade(Scene):
    def construct(self):
        axes = Axes(x_range=[-10,10],x_length=10,y_range=[-3,3], y_length=5, axis_config={'include_tip':True}).set_color('BLUE')
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")

        
        seno=MathTex("f(x)=sen(x)", font_size=36, color=YELLOW).shift(2.5*UP+3*RIGHT)
        senao=axes.plot(lambda x: sin(x),x_range=[-3*pi,3*pi], color=YELLOW )


        #TEXTOS#
        conc=MathTex("Intervalos\ de\ Concavidade:", font_size=36, color=WHITE).shift(3.25*UP)
        concposi=MathTex("\\text{Intervalos onde a concavidade da função seno é positiva}",color=WHITE,font_size=28).shift(3*DOWN)
        concneg=MathTex("\\text{Intervalos onde a concavidade da função seno é negativa}",color=WHITE,font_size=28).shift(3*DOWN)
        inflexao=Tex("Pontos de inflexão", color=WHITE, font_size=36).shift(3.25*UP)
        inflexao2=MathTex("\\text{São os pontos onde muda a concavidade da função. Os pontos da forma:}\ (\pi n,0)\ para\ n\ inteiro}",color=WHITE,font_size=28).shift(3*DOWN)
        
        #GRAPH# 
        graphpos1=axes.plot(lambda x: sin(x),x_range=[-3*pi,-2*pi], color=BLUE)
        graphpos2=axes.plot(lambda x: sin(x),x_range=[-pi,0], color=BLUE )
        graphpos3=axes.plot(lambda x: sin(x),x_range=[pi,2*pi], color=BLUE )

        graphneg1=axes.plot(lambda x: sin(x),x_range=[-2*pi,-pi], color=RED)
        graphneg2=axes.plot(lambda x: sin(x),x_range=[0,pi], color=RED)
        graphneg3=axes.plot(lambda x: sin(x),x_range=[2*pi,3*pi], color=RED)

        #PONTOS DE INFLEXÃO

        ponto1=Dot(axes.c2p(-3*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        label1=MathTex("(-3\pi,0)", color=WHITE, font_size=20).next_to(ponto1, DOWN + RIGHT, buff=0.2)

        ponto2=Dot(axes.c2p(-2*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        label2=MathTex("(-2\pi,0)", color=WHITE, font_size=20).next_to(ponto2, DOWN+RIGHT, buff=0.2)

        ponto3=Dot(axes.c2p(-pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label3=MathTex("(-\pi,0)", color=WHITE, font_size=20).next_to(ponto3, DOWN+RIGHT, buff=0.2)

        ponto4=Dot(axes.c2p(0,0), color=RED, fill_opacity=5, stroke_width=1)
        label4=MathTex("(0,0)", color=WHITE, font_size=20).next_to(ponto4, DOWN+RIGHT, buff=0.2)

        ponto5=Dot(axes.c2p(pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label5=MathTex("(\pi,0)", color=WHITE, font_size=20).next_to(ponto5, DOWN+RIGHT, buff=0.2)

        ponto6=Dot(axes.c2p(2*pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label6=MathTex("(2\pi,0)", color=WHITE, font_size=20).next_to(ponto6, DOWN+RIGHT, buff=0.2)

        ponto7=Dot(axes.c2p(3*pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label7=MathTex("(3\pi,0)", color=WHITE, font_size=20).next_to(ponto7, DOWN+RIGHT, buff=0.2)

        grupo_pontos=VGroup(ponto1,label1,ponto2,label2,ponto3,label3,ponto4,label4,ponto5,label5,ponto6,label6,)
    

        #ANIMAÇÃO
        self.play(Create(axes),Create(axes_label))
        self.play(Write(seno))
        self.play(Create(senao),run_time=3)
        self.play(Write(conc))
        self.play(Create(graphpos1),run_time=2)
        self.play(Create(graphpos2),run_time=2)
        self.play(Create(graphpos3),run_time=2)
        self.play(Create(grupo_pontos),run_time=2)
        self.play(FadeOut(senao),Write(concposi))
        self.wait(4)
        self.play(FadeOut(grupo_pontos))
        self.play(FadeOut(graphpos1),FadeOut(graphpos2),FadeOut(graphpos3),FadeOut(concposi))
        self.play(Create(senao),run_time=3)
        self.play(Create(grupo_pontos),FadeOut(ponto1),FadeOut(label1))
        self.play(Create(graphneg1),run_time=2)
        self.play(Create(graphneg2),run_time=2)
        self.play(Create(graphneg3),run_time=2)
        self.play(FadeOut(senao),Write(concneg))
        self.wait(3)
        self.play(FadeOut(grupo_pontos))
        self.play(FadeOut(conc),FadeOut(concneg),FadeOut(graphneg1),FadeOut(graphneg2),FadeOut(graphneg3))
      
        self.wait(0.5)
        self.play(Write(inflexao))
        self.play(Create(ponto1),Create(label1))
        self.play(Create(graphpos1))
        self.play(Create(ponto2),Create(label2))
        self.play(Create(graphneg1))     
        self.play(Create(ponto3),Create(label3))
        self.play(Create(graphpos2))
        self.play(Create(ponto4),Create(label4))
        self.play(Create(graphneg2))
        self.play(Create(ponto5),Create(label5))
        self.play(Create(graphpos3))
        self.play(Create(ponto6),Create(label6))
        self.play(Create(graphneg3))
        self.play(Create(ponto7),Create(label7))


        self.play(Write(inflexao2))
        self.wait(5)


        
       