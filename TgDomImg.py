from manim import *
from numpy import *

class TgDomImg(Scene):
    def construct(self):
        #COORDENADAS
        axes = Axes(x_range=[-3*pi,3*pi],x_length=10,y_range=[-10,10], y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
                
        #OBJETOS
        #Ter 2 graficos iguais está me incomodando. Preciso ver como usar a mesma variável duas vezes...
        point1 = Dot(axes.c2p(-5*pi/2-0.1,0), color=WHITE, fill_opacity=5,stroke_width=2)
        point2 = Dot(axes.c2p(-3*pi/2-0.1,0), color=WHITE, fill_opacity=5,stroke_width=2)
        point3 = Dot(axes.c2p(-pi/2-0.1,0), color=WHITE, fill_opacity=5,stroke_width=2)
        point4 = Dot(axes.c2p(pi/2+0.1,0), color=WHITE, fill_opacity=5,stroke_width=2)
        point5 = Dot(axes.c2p(((3*pi)/2+0.05),0), color=WHITE, fill_opacity=5,stroke_width=2)
        point6 = Dot(axes.c2p(((5*pi)/2+0.05),0), color=WHITE, fill_opacity=5,stroke_width=2)
        
        imagem=Line(axes.c2p(0,-10), axes.c2p(0,10),stroke_width = 6, stroke_color = RED )

        dominio0= Line(axes.c2p(-3*pi,0), axes.c2p(-5*pi/2-0.1,0),stroke_width = 6, stroke_color = RED )
        dominio= Line(axes.c2p(-5*pi/2+0.1,0), axes.c2p(-3*pi/2-0.05,0),stroke_width = 6, stroke_color = RED )
        dominio2=Line(axes.c2p(-3*pi/2+0.1,0), axes.c2p(-pi/2-0.05,0),stroke_width = 6, stroke_color = RED )
        dominio3= Line(axes.c2p(-pi/2+0.1,0), axes.c2p(pi/2-0.05,0),stroke_width = 6, stroke_color = RED )
        dominio4=Line(axes.c2p(pi/2+0.1,0), axes.c2p(((3*pi)/2-0.1),0),stroke_width = 6, stroke_color = RED )
        dominio5= Line(axes.c2p(((3*pi)/2)+0.1,0), axes.c2p((5*pi/2-0.1),0),stroke_width = 6, stroke_color = RED )
        dominio6= Line(axes.c2p((((5*pi/2)+0.1))+0.1,0), axes.c2p(3*pi,0),stroke_width = 6, stroke_color = RED )

        #ANIMAÇÃO DOMINIO
        graph0 = axes.plot((lambda x: tan(x)), x_range=[-3*pi,(-5*pi/2)-0.10], color=RED, stroke_width=5)
        graph = axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,(-3*pi/2)-0.10], color=RED, stroke_width=5)
        graph2 = axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,(-pi/2)-0.10], color=RED, stroke_width=5)
        graph3 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        graph4 = axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,((3*pi)/2)-0.10], color=RED, stroke_width=5)
        graph5 = axes.plot((lambda x: tan(x)), x_range=[(3*pi/2)+0.10,(5*pi/2)-0.10], color=RED, stroke_width=5)
        graph51 = axes.plot((lambda x: tan(x)), x_range=[(5*pi/2)+0.10,3*pi], color=RED, stroke_width=5)
       
        #ANIMAÇÃO IMAGEM
        graph52 = axes.plot((lambda x: tan(x)), x_range=[-3*pi,(-5*pi/2)-0.10], color=RED, stroke_width=5)
        graph6 = axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,(-3*pi/2)-0.10], color=RED, stroke_width=5)
        graph7 = axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,(-pi/2)-0.10], color=RED, stroke_width=5)
        graph8 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        graph9 = axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,((3*pi)/2)-0.10], color=RED, stroke_width=5)
        graph10 = axes.plot((lambda x: tan(x)), x_range=[(3*pi/2)+0.10,(5*pi/2)-0.10], color=RED, stroke_width=5)
        graph11 = axes.plot((lambda x: tan(x)), x_range=[(5*pi/2)+0.10,3*pi], color=RED, stroke_width=5)
        
        #TEXTOS
        
        mathtext1= MathTex("f(x)=tg(x)").set_color_by_gradient(RED).set_height(0.5).shift(UP*3.5)

        domtext= MathTex("D_f=\mathbb{R}\setminus\ \{\\frac{\pi}{2}+k\pi \,: \ k \; inteiro\}", font_size= 36).shift(UP*1.98+LEFT*3)
        imgtext= MathTex("Im_f=\mathbb{R}").shift(UP*1.98+LEFT*3)

        label1 = MathTex("(\\frac{-5\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point1, DOWN, buff=0.2)
        label2 = MathTex("(\\frac{-3\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point2, DOWN, buff=0.2)
        label3 = MathTex("(\\frac{-\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point3, DOWN, buff=0.2)
        label4 = MathTex("(\\frac{\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point4, DOWN, buff=0.2)
        label5 = MathTex("(\\frac{3\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point5, DOWN, buff=0.2)
        label6 = MathTex("(\\frac{5\pi}{2}, 0)", color=WHITE, font_size=20).next_to(point6, DOWN , buff=0.2)
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")
        

        #animação começa aqui
        self.play(DrawBorderThenFill(axes))
        self.play(Write(axis_labels))
        self.play(Write(mathtext1),run_time=0.5)
        self.wait(2)
        self.play(Create(graph0), run_time=1)
        self.play(Create(graph), run_time=1)
        self.play(Create(graph2), run_time=1)
        self.play(Create(graph3), run_time=1)
        self.play(Create(graph4), run_time=1)
        self.play(Create(graph5), run_time=1)
        self.play(Create(graph51), run_time=1)
        self.wait(3)
    

        self.play(Transform(graph0, dominio0),Transform(graph, dominio),Transform(graph2, dominio2),Transform(graph3, dominio3),Transform(graph4, dominio4),Transform(graph5, dominio5),Transform(graph51, dominio6),run_time=5)
        self.wait(2)
        self.play(Create(point1),Create(point2),Create(point3),Create(point4),Create(point5),Create(point6))
        self.wait(2)
        
        self.play(Create(label1),Create(label2),Create(label3),Create(label4),Create(label5),Create(label6))
        self.wait(4)
        self.play(Transform(label1,domtext),Transform(label2,domtext),Transform(label3,domtext),Transform(label4,domtext),Transform(label5,domtext),Transform(label6,domtext),run_time=2)
        self.wait(3)
        self.play(FadeOut(domtext),FadeOut(point1),FadeOut(point2),FadeOut(point3),FadeOut(point4),FadeOut(point5),FadeOut(point6),run_time=0.5)
        self.play(FadeOut(label1),FadeOut(label3),FadeOut(label4),FadeOut(label5),FadeOut(label2),FadeOut(label6),run_time=0.5)
        self.wait(1)
        self.play(FadeOut(graph0),FadeOut(graph),FadeOut(graph2),FadeOut(graph3),FadeOut(graph4),FadeOut(graph5),FadeOut(graph51),run_time=0.5)
        
        self.play(Create(graph52), run_time=1)
        self.play(Create(graph6), run_time=1)
        self.play(Create(graph7), run_time=1)
        self.play(Create(graph8), run_time=1)
        self.play(Create(graph9), run_time=1)
        self.play(Create(graph10), run_time=1)
        self.play(Create(graph11), run_time=1)
        self.wait(3)
    

        self.play(Transform(graph52, imagem),Transform(graph6, imagem),Transform(graph7, imagem),Transform(graph8, imagem),Transform(graph9, imagem),Transform(graph10, imagem),Transform(graph11, imagem),run_time=2)

        self.play(Write(imgtext))
        self.wait(2)
        
        self.wait(2)

        
        
    