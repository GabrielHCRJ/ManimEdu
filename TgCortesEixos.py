from manim import *
from numpy import *

class TgCortesEixos(Scene):
    def construct(self):
        axes = Axes(x_range=[-3*pi,3*pi],x_length=10,y_range=[-10,10], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")

        

        tg1 = axes.plot((lambda x: tan(x)), x_range=[-3*pi,(-5*pi/2)-0.10], color=RED, stroke_width=5)
        tg2 = axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,(-3*pi/2)-0.10], color=RED, stroke_width=5)
        tg3 = axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,(-pi/2)-0.10], color=RED, stroke_width=5)
        tg4 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        tg5 = axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,((3*pi)/2)-0.10], color=RED, stroke_width=5)
        tg6 = axes.plot((lambda x: tan(x)), x_range=[(3*pi/2)+0.10,(5*pi/2)-0.10], color=RED, stroke_width=5)
        tg7 = axes.plot((lambda x: tan(x)), x_range=[(5*pi/2)+0.10,3*pi], color=RED, stroke_width=5)

        mathtext1= MathTex("f(x)=tg(x)",font_size=28).set_color_by_gradient(RED).set_height(0.5).shift(UP*2.5+RIGHT*2.5)
        
        text= MathTex("Pontos\ de\ corte\ com\ os\ eixos\ coordenados:", font_size= 28,color=WHITE).shift(UP*3.5)
        pontosx=MathTex("Eixo\ x:(-3\pi,0),(-2\pi,0),(-\pi,0)...(k\pi,0)|\ k\ inteiro",font_size= 22).shift(3*DOWN)
        pontosy=MathTex("Eixo\ y:(0,0)",font_size=22).next_to(pontosx,DOWN)

        point = Dot(axes.c2p(-3*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        point2 = Dot(axes.c2p(-2*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        point3 = Dot(axes.c2p(-pi,0), color=RED, fill_opacity=5,stroke_width=1)
        point4 = Dot(axes.c2p(0,0), color=RED, fill_opacity=5,stroke_width=1)
        point5 = Dot(axes.c2p(pi,0), color=RED, fill_opacity=5,stroke_width=1)
        point6 = Dot(axes.c2p(2*pi,0), color=RED, fill_opacity=5,stroke_width=1)
        
        label = MathTex("(-3\pi, 0)", color=WHITE, font_size=20).next_to(point, DOWN + RIGHT, buff=0.2)
        label2 = MathTex("(-2\pi, 0)", color=WHITE, font_size=20).next_to(point2, DOWN + RIGHT, buff=0.2)
        label3 = MathTex("(-\pi, 0)", color=WHITE, font_size=20).next_to(point3, DOWN + RIGHT, buff=0.2)
        label4 = MathTex("(0, 0)", color=WHITE, font_size=20).next_to(point4, DOWN + RIGHT, buff=0.2)
        label5 = MathTex("(\pi, 0)", color=WHITE, font_size=20).next_to(point5, DOWN + RIGHT, buff=0.2)
        label6 = MathTex("(2\pi, 0)", color=WHITE, font_size=20).next_to(point6, DOWN + RIGHT, buff=0.2)

        self.play(DrawBorderThenFill(axes))
        self.play(Write(axis_labels))
       
     
        self.play(Create(mathtext1),run_time=1)
        self.play(Write(text),run_time=3)
        self.play(Create(tg1))
        self.play(Create(tg2))
        self.play(Create(tg3))
        self.play(Create(tg4))
        self.play(Create(tg5))
        self.play(Create(tg6))
        self.play(Create(tg7))

        self.play(Create(point),Create(point2),Create(point3),Create(point4),Create(point5),Create(point6),run_time=2)
        self.wait(2)
        self.play(Indicate(point),Indicate(point2),Indicate(point3),Indicate(point4),Indicate(point5),Indicate(point6),run_time=3)
        self.wait(2)
        self.play(Indicate(point4))
        self.wait(2)
        self.play(Create(label),Create(label2),Create(label3),Create(label4),Create(label5),Create(label6))
        
        self.play(Create(pontosx),run_time=2)
        self.play(Create(pontosy),run_time=2)
        self.wait(5)
       
        
        
    