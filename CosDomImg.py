from manim import *
from numpy import *

class CosDomImg(Scene):
    def construct(self):
        #COORDENADAS
        axes = Axes(x_range=[-10,10],x_length=10,y_range=[-3,3], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
                
        #OBJETOS
        #Ter 2 graficos iguais está me incomodando. Preciso ver como usar a mesma variável duas vezes...
        point1 = Dot(axes.c2p(0,1), color=RED)
        point2 = Dot(axes.c2p(0,-1), color=RED)
        dominio= Line(axes.c2p(-10,0), axes.c2p(10,0),stroke_width = 6, stroke_color = RED )
        imagem=Line(axes.c2p(0,-1), axes.c2p(0,1),stroke_width = 6, stroke_color = RED )
        graph = axes.plot((lambda x: cos(x)), x_range=[-10, 10], color=RED)
        graph2 = axes.plot((lambda x: cos(x)), x_range=[-10, 10], color=RED)

        #TEXTOS
        mathtext1= MathTex("f(x)=cos(x)").set_color_by_gradient(RED).set_height(0.5)
        domtext= MathTex("D_f=\mathbb{R}")
        imgtext= MathTex("Im(f)=[-1,1]")
        label1 = MathTex("(0, 1)", color=WHITE, font_size=20).next_to(point1, UP + RIGHT, buff=0.2)
        label2 = MathTex("(0, -1)", color=WHITE, font_size=20).next_to(point2, DOWN + RIGHT, buff=0.2)
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")
        
        self.play(DrawBorderThenFill(axes))
        self.play(Write(axis_labels))
       
        self.play(mathtext1.animate.shift(UP*2+RIGHT*2.5),run_time=1)
        self.play(Create(graph), run_time=2)
        
       
        self.wait(2)
        self.play(Transform(graph, dominio),run_time=3)
        self.play(domtext.animate.shift(UP*2+LEFT*2),run_time=1)
        self.wait()
        self.play(FadeOut(domtext))
        self.play(FadeOut(graph))

        self.play(Create(graph2), run_time=2)
        self.wait(2)
        self.play(Transform(graph2, imagem),run_time=3)
        self.play(imgtext.animate.shift(UP*1.98+LEFT*2.75),run_time=1)
        
        self.play(FadeIn(point1), FadeIn(label1),FadeIn(point2), FadeIn(label2))
        self.wait(4)

        
        
    