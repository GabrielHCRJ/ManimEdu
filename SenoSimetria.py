from manim import *
from numpy import *
##COMO FAÇO O PONTO GIRAR JUNTO COM A FUNÇÃO?##
class SenoSimetria(Scene):
    def construct(self):
        
        axes = Axes(x_range=[-10,10],x_length=10,y_range=[-3,3], y_length=5, axis_config={'include_tip':True}).set_color('BLUE')
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")

        graph=axes.plot((lambda x: sin(x)), x_range=[-10,10], stroke_width=7, color=RED)
        graph1=axes.plot(lambda x: sin(x), x_range=[-10,10], color=BLUE)
        simetria=MathTex("Simetria:",font_size=36).shift(3.25*UP)

        x=ValueTracker(1)
        #TESTE
        angle = 180*DEGREES

        r=ValueTracker(1)
        ponto1=Dot(axes.c2p(pi/2,sin(pi/2)), color=RED)
        ponto2=Dot(axes.c2p(-pi/2,-sin(pi/2)), color=RED)
        grupo=VGroup(graph,ponto1)
        grupo2=VGroup(graph1,ponto2)
        line1 = DashedLine(start=axes.c2p(pi/2,0),end=axes.c2p(pi/2,1))
        line2 = DashedLine(start=axes.c2p(0,1),end=axes.c2p(pi/2,1))

        line3 = DashedLine(start=axes.c2p(-pi/2,0),end=axes.c2p(-pi/2,-1))
        line4 = DashedLine(start=axes.c2p(0,-1),end=axes.c2p(-pi/2,-1))

        label1=MathTex("(x,sen(x))", color=WHITE, font_size=20).next_to(ponto1, UP + RIGHT, buff=0.2)
        label2=MathTex("(-x,-sen(x))", color=WHITE, font_size=20).next_to(ponto2, DOWN + LEFT, buff=0.2)
       
        
     #

        resposta=Text("Função Ímpar:",font_size=22).shift(3*RIGHT+2.5*UP)
        resposta2=Text("Simétrica em relação à origem ",font_size=22).shift(3*RIGHT+2*UP)
        resposta3=MathTex("sen(-x)=-sen(x)",font_size=26).shift(3*RIGHT+1.5*UP)
        seno=MathTex("f(x)=sen(x)",font_size=28,color=RED).shift(2.5*UP+2.5*LEFT).set_height(0.5)
        
        
        self.play(Create(axes),Write(axis_labels),run_time=2)
        self.play(Create(simetria))
        self.wait()
        self.play(Write(seno))
        self.play(Create(graph1),Create(graph),run_time=2)
        self.play(Create(line1),Create(line2))
        self.play(Create(ponto1))
        
        self.play(Write(label1))
        self.play(Create(ponto2))
        self.play(Create(label2))
        self.wait(1.5)
        self.play(FadeOut(line1),FadeOut(line2),FadeOut(label1))


        self.play(Rotate(grupo,angle),grupo2.animate.shift(UP*0.07),run_time=4)
        self.remove(grupo2)
        self.play(Create(line3),Create(line4))

        
        self.wait(2)
        self.play(FadeOut(line3),FadeOut(line4),FadeOut(label2))
        
        
        
        self.wait()
        self.play(Create(resposta))
        self.play(Create(resposta2))
        self.play(Create(resposta3))
        self.wait(4)