from manim import *
from numpy import *

class CosCorteEixos(Scene):
    def construct(self):
        axes = Axes(x_range=[-10,10],x_length=10,y_range=[-3,3], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")
        cosseno = axes.plot((lambda x: cos(x)), x_range=[-10, 10], color=RED)

        mathtext1= MathTex("f(x)=cos(x)",font_size=28).set_color_by_gradient(RED).set_height(0.5).shift(UP*2.5+RIGHT*2.5)
        
        text= MathTex("Pontos\ de\ corte\ com\ os\ eixos\ coordenados:", font_size= 28,color=WHITE).shift(UP*3.5)
        pontos=MathTex("Eixo\ x:(\\frac{-5\pi}{2}, 0),(\\frac{-3\pi}{2}, 0),(\\frac{-\pi}{2}, 0)...(k\pi+\\frac{\pi}{2}, 0)",font_size= 20,color=WHITE).shift(UP*2.5+LEFT*3)
        pontosy=MathTex("Eixo\ y: (0,1)",font_size= 20,color=WHITE).shift(UP*2+LEFT*3) 

        point = Dot(axes.c2p(-5*pi/2,0), color=RED, fill_opacity=5,stroke_width=1)
        point2 = Dot(axes.c2p(-3*pi/2,0), color=RED, fill_opacity=5,stroke_width=1)
        point3 = Dot(axes.c2p(-pi/2,0), color=RED, fill_opacity=5,stroke_width=1)
        point4 = Dot(axes.c2p(pi/2,0), color=RED, fill_opacity=5,stroke_width=1)
        point5 = Dot(axes.c2p(3*pi/2,0), color=RED, fill_opacity=5,stroke_width=1)
        point6 = Dot(axes.c2p(5*pi/2,0), color=RED, fill_opacity=5,stroke_width=1)
        point7= Dot(axes.c2p(0,1), color=RED, fill_opacity=5, stroke_width=1)
        
        label = MathTex("(\\frac{-5\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point, DOWN + RIGHT, buff=0.2)
        label2 = MathTex("(\\frac{-3\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point2, DOWN + RIGHT, buff=0.2)
        label3 = MathTex("(\\frac{-\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point3, DOWN + RIGHT, buff=0.2)
        label4 = MathTex("(\\frac{\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point4, DOWN + RIGHT, buff=0.2)
        label5 = MathTex("(\\frac{3\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point5, DOWN + RIGHT, buff=0.2)
        label6 = MathTex("(\\frac{5\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point6, DOWN + RIGHT, buff=0.2)
        label7 = MathTex("(0,1)", color=WHITE, font_size=20).next_to(point7, UP + RIGHT, buff=0.2)

        label_grupo = VGroup(label,label2,label3,label4,label5,label6)

        self.play(DrawBorderThenFill(axes))
        self.play(Write(axis_labels))
       
     
        self.play(Create(mathtext1),run_time=1)
        self.play(Write(text),run_time=1)
        self.play(Create(cosseno), run_time=3)
        self.play(Create(point),Create(point2),Create(point3),Create(point4),Create(point5),Create(point6))
        self.wait(2)
        self.play(Indicate(point),Indicate(point2),Indicate(point3),Indicate(point4),Indicate(point5),Indicate(point6),run_time=1)
        self.play(Indicate(point7))
        self.wait(2)
        self.play(Create(label),Create(label2),Create(label3),Create(label4),Create(label5),Create(label6),Create(label7))
        self.wait(2)
        
        self.play(Transform(label_grupo,pontos))
        self.play(Transform(label7,pontosy))
        self.wait(5)
       
        
        
    