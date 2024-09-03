from manim import *
from numpy import *

class CosConcavidade(Scene):
    def construct(self):
        axes = Axes(x_range=[-7/2*pi,7/2*pi], x_length=10, y_range=[-3,3],y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")

        
        cosseno=MathTex("f(x)=cos(x)", font_size=36, color=RED).shift(2.5*UP+3*RIGHT)
        cossenao=axes.plot(lambda x: cos(x),x_range=[-7/2*pi,7/2*pi], color=RED )


        #TEXTOS#
        conc=MathTex("Intervalos\ de\ Concavidade:", font_size=36, color=WHITE).shift(3.25*UP)
        concposi=MathTex("\\text{Intervalos onde a concavidade da função cosseno é positiva}",color=WHITE,font_size=28).shift(3*DOWN)
        concneg=MathTex("\\text{Intervalos onde a concavidade da função cosseno é negativa}",color=WHITE,font_size=28).shift(3*DOWN)
        inflexao=Tex("Pontos de inflexão", color=WHITE, font_size=36).shift(3.25*UP)
        inflexao2=MathTex("\\text{São os pontos onde muda a concavidade da função. Os pontos da forma:}\ (k\\pi+\\frac{\\pi}{2},0)\ para\ k\ inteiro}",color=WHITE,font_size=28).shift(3*DOWN)
        
        #GRAPH# 
        graphpos1=axes.plot(lambda x: cos(x),x_range=[-7/2*pi,-5/2*pi], color=BLUE)
        graphpos2=axes.plot(lambda x: cos(x),x_range=[-3*pi/2,-pi/2], color=BLUE )
        graphpos3=axes.plot(lambda x: cos(x),x_range=[pi/2,3/2*pi], color=BLUE )
        graphpos4=axes.plot(lambda x: cos(x),x_range=[5*pi/2,7/2*pi], color=BLUE )

        graphneg1=axes.plot(lambda x: cos(x),x_range=[-5/2*pi,-3*pi/2], color=RED)
        graphneg2=axes.plot(lambda x: cos(x),x_range=[-pi/2,pi/2], color=RED)
        graphneg3=axes.plot(lambda x: cos(x),x_range=[3*pi/2,5*pi/2], color=RED)
        

        #PONTOS DE INFLEXÃO

        ponto1=Dot(axes.c2p(-7/2*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        label1=MathTex("(\\frac{-7\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto1, DOWN + LEFT, buff=0.2)

        ponto2=Dot(axes.c2p(-5/2*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        label2=MathTex("(\\frac{-5\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto2, UP+LEFT, buff=0.2)

        ponto3=Dot(axes.c2p(-3/2*pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label3=MathTex("(\\frac{-3\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto3, DOWN+LEFT, buff=0.2)

        ponto4=Dot(axes.c2p(-pi/2,0), color=RED, fill_opacity=5, stroke_width=1)
        label4=MathTex("(\\frac{-\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto4, UP+LEFT, buff=0.2)

        ponto5=Dot(axes.c2p(pi/2,0), color=RED, fill_opacity=5, stroke_width=1)
        label5=MathTex("(\\frac{\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto5, DOWN+LEFT, buff=0.2)

        ponto6=Dot(axes.c2p(3/2*pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label6=MathTex("(\\frac{3\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto6, UP+LEFT, buff=0.2)

        ponto7=Dot(axes.c2p(5/2*pi,0), color=RED, fill_opacity=5, stroke_width=1)
        label7=MathTex("(\\frac{5\pi}{2},0)", color=WHITE, font_size=20).next_to(ponto7, DOWN+LEFT, buff=0.2)

        #grupo_pontos=VGroup(ponto1,ponto2,ponto3,ponto4,ponto5,ponto6,ponto7)
        grupo_pontos=VGroup(ponto1,label1,ponto2,label2,ponto3,label3,ponto4,label4,ponto5,label5,ponto6,label6,ponto7,label7)
    

        #ANIMAÇÃO
        self.play(Create(axes),Create(axes_label))
        self.play(Write(cosseno))
        self.play(Create(cossenao),run_time=3)
        self.play(Write(conc))
        self.play(Create(graphpos1))
        self.play(Create(graphpos2))
        self.play(Create(graphpos3))
        self.play(Create(graphpos4))
        self.play(Create(grupo_pontos),run_time=4)
        self.play(FadeOut(cossenao),Write(concposi))
        self.wait(4)
        self.play(FadeOut(grupo_pontos))
        self.play(FadeOut(graphpos1),FadeOut(graphpos2),FadeOut(graphpos3),FadeOut(graphpos4),FadeOut(concposi))
        self.play(Create(cossenao),run_time=3)
        self.play(Create(grupo_pontos),FadeOut(ponto1),run_time=3)
        self.play(Create(graphneg1))
        self.play(Create(graphneg2))
        self.play(Create(graphneg3))
       
        self.play(FadeOut(cossenao),Write(concneg))
        self.wait(3)
        self.play(FadeOut(grupo_pontos))
        self.play(FadeOut(conc),FadeOut(concneg),FadeOut(graphneg1),FadeOut(graphneg2),FadeOut(graphneg3))
      
        self.wait(0.5)
        self.play(Write(inflexao))
        self.play(Create(ponto1),Write(label1))
        #self.play(Create(ponto1))
        self.play(Create(graphpos1))
        #self.play(Create(ponto2))
        self.play(Create(ponto2),Write(label2))
        self.play(Create(graphneg1))     
        #self.play(Create(ponto3))
        self.play(Create(ponto3),Write(label3))
        self.play(Create(graphpos2))
        #self.play(Create(ponto4))
        self.play(Create(ponto4),Write(label4))
        self.play(Create(graphneg2))
        #self.play(Create(ponto5))
        self.play(Create(ponto5),Write(label5))
        self.play(Create(graphpos3))
        #self.play(Create(ponto6))
        self.play(Create(ponto6),Write(label6))
        self.play(Create(graphneg3))
        #self.play(Create(ponto7))
        self.play(Create(graphpos4))
        self.play(Create(ponto7),Write(label7))
        self.play(Write(inflexao2))


        
        self.wait(5)


        
       