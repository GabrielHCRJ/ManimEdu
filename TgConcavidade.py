from manim import *
from numpy import *

class TgConcavidade(Scene):
    def construct(self):
        axes = Axes(x_range=[-3*pi,3*pi], x_length=10, y_range=[-10,10], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")

        
        seno=MathTex("f(x)=tg(x)", font_size=36, color=RED).shift(2.5*UP+3*RIGHT)

        #GRAFICO TANGENTE
        tg1 = axes.plot((lambda x: tan(x)), x_range=[-3*pi,(-5*pi/2)-0.10], color=RED, stroke_width=5)
        tg2 = axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,(-3*pi/2)-0.10], color=RED, stroke_width=5)
        tg3 = axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,(-pi/2)-0.10], color=RED, stroke_width=5)
        tg4 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        tg5 = axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,((3*pi)/2)-0.10], color=RED, stroke_width=5)
        tg6 = axes.plot((lambda x: tan(x)), x_range=[(3*pi/2)+0.10,(5*pi/2)-0.10], color=RED, stroke_width=5)
        tg7 = axes.plot((lambda x: tan(x)), x_range=[(5*pi/2)+0.10,3*pi], color=RED, stroke_width=5)


        #TEXTOS#
        conc=MathTex("Intervalos\ de\ Concavidade:", font_size=36, color=WHITE).shift(3.25*UP)
        concposi=MathTex("\\text{Intervalos onde a concavidade da função tangente é positiva}",color=WHITE,font_size=28).shift(3*DOWN)
        concneg=MathTex("\\text{Intervalos onde a concavidade da função tangente é negativa}",color=WHITE,font_size=28).shift(3*DOWN)
        inflexao=Tex("Pontos de inflexão", color=WHITE, font_size=36).shift(3.25*UP)
        inflexao2=MathTex("\\text{São os pontos onde muda a concavidade da função. Os pontos da forma:}\ (n\pi ,0)\ para\ n\ inteiro}",color=WHITE,font_size=28).shift(3*DOWN)
        
        #GRAPH# 
        graphpos1=axes.plot(lambda x: tan(x),x_range=[-3*pi,(-5*pi/2)-0.10], color=BLUE)
        graphpos2=axes.plot(lambda x: tan(x),x_range=[(-2*pi)+0.10,(-3*pi/2)-0.10], color=BLUE )
        graphpos3=axes.plot(lambda x: tan(x),x_range=[-pi+0.10,((-pi)/2)-0.10], color=BLUE )
        graphpos4=axes.plot(lambda x: tan(x),x_range=[0.10,((pi)/2)-0.10], color=BLUE )
        graphpos5=axes.plot(lambda x: tan(x),x_range=[pi+0.10,((3*pi)/2)-0.10], color=BLUE )
        graphpos6=axes.plot((lambda x: tan(x)), x_range=[2*pi+0.10,(5*pi/2)-0.10], color=BLUE, stroke_width=5)

        graphneg1=axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,-2*pi], color=RED, stroke_width=5)
        graphneg2=axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,-pi-0.10], color=RED, stroke_width=5)
        graphneg3=axes.plot((lambda x: tan(x)), x_range=[-pi/2+0.10,-0.1], color=RED, stroke_width=5)
        graphneg4=axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,pi], color=RED, stroke_width=5)
        graphneg5=axes.plot((lambda x: tan(x)), x_range=[3*pi/2+0.10,2*pi], color=RED, stroke_width=5)
        graphneg6=axes.plot((lambda x: tan(x)), x_range=[5*pi/2+0.10,3*pi], color=RED, stroke_width=5)
       
        
        


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
        #grupo_pontos=VGroup(ponto1,ponto2,ponto3,ponto4,ponto5,ponto6)
    

        #ANIMAÇÃO
        self.play(Create(axes),Create(axes_label))
        self.play(Write(seno))
        self.play(Create(tg1))
        self.play(Create(tg2))
        self.play(Create(tg3))
        self.play(Create(tg4))
        self.play(Create(tg5))
        self.play(Create(tg6))
        self.play(Create(tg7))

        self.play(Write(conc))
        self.play(Create(graphpos1))
        self.play(Create(graphpos2))
        self.play(Create(graphpos3))
        self.play(Create(graphpos4))
        self.play(Create(graphpos5))
        self.play(Create(graphpos6))
        self.wait(3)
        self.play(Create(grupo_pontos),run_time=3)
        self.play(Write(concposi))
        self.wait(2)
        self.play(FadeOut(tg1),FadeOut(tg2),FadeOut(tg3),FadeOut(tg4),FadeOut(tg5),FadeOut(tg6),FadeOut(tg7))
        self.play(FadeOut(graphpos1),FadeOut(graphpos2),FadeOut(graphpos3),FadeOut(graphpos4),FadeOut(graphpos5),FadeOut(graphpos6),FadeOut(concposi))
        self.wait(3)
 

        
        
        self.play(Create(tg1))
        self.play(Create(tg2))
        self.play(Create(tg3))
        self.play(Create(tg4))
        self.play(Create(tg5))
        self.play(Create(tg6))
        self.play(Create(tg7))
        self.wait(2)
        self.play(FadeOut(grupo_pontos))
    
        self.play(Create(graphneg1))
        self.play(Create(graphneg2))
        self.play(Create(graphneg3))
        self.play(Create(graphneg4))
        self.play(Create(graphneg5))
        self.play(Create(graphneg6))
        self.wait(2)
       
        self.play(Write(concneg))
        self.wait(3)
        self.play(FadeOut(grupo_pontos))
        self.play(FadeOut(conc),FadeOut(concneg),FadeOut(graphneg1),FadeOut(graphneg2),FadeOut(graphneg3),FadeOut(graphneg4),FadeOut(graphneg5),FadeOut(graphneg6))
      
        self.wait(0.5)
        self.play(Write(inflexao))
        self.play(Create(ponto1),Write(label1))
        self.play(Create(graphpos1))
        self.play(Create(graphneg1)) 
        self.play(Create(ponto2),Write(label2))
        self.play(Create(graphpos2))  
        self.play(Create(graphneg2)) 
        self.play(Create(ponto3),Write(label3))
        self.play(Create(graphpos3))
        self.play(Create(graphneg3))
        self.play(Create(ponto4),Write(label4))
        self.play(Create(graphpos4))
        self.play(Create(graphneg4))
        self.play(Create(ponto5),Write(label5))
        self.play(Create(graphpos5))
        self.play(Create(graphneg5))
        self.play(Create(ponto6),Write(label6))
        self.play(Create(graphpos6))
        self.play(Create(graphneg6))
        self.play(Create(ponto7),Write(ponto7))


        self.play(Write(inflexao2))
        self.wait(5)


        
       