from manim import *
from numpy import *

class SenoCortesEixos(Scene):
    def construct(self):
        
        #graficos
        axes = Axes(x_range=[-10,10],x_length=10,y_range=[-3,3], y_length=5, axis_config={'include_tip':True}).set_color('BLUE')
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")
        graph = axes.plot((lambda x: sin(x)), x_range=[-10, 10], color=RED)

        #textos
        mathtext1= MathTex("f(x)=sen(x)",font_size=28).set_color_by_gradient(RED).set_height(0.5).shift(UP*2.5+RIGHT*2.5)
        text= MathTex("Pontos\ de\ corte\ com\ os\ eixos\ coordenados:", font_size= 28).shift(UP*3.2)
        pontosx=MathTex("Eixo\ x:(-3\pi,0),(-2\pi,0),(-\pi,0)...(k\pi,0)|\ k\ inteiro",font_size= 22).shift(UP*2.5+LEFT*3)
        pontosy=MathTex("Eixo\ y:(0,0)",font_size=22).next_to(pontosx,DOWN)
      
              
               
       
        #ANIMAÇÃO COMEÇA AQUI

        self.play(DrawBorderThenFill(axes))
        self.play(Write(axis_labels))
        self.play(Create(mathtext1),run_time=1)
        self.play(Write(text),run_time=1)
     

        self.play(Create(graph), run_time=4)

        for i in range(0,6):
            self.play(Create(Dot(axes.c2p(i*pi-3*pi,0), color=RED_E, fill_opacity=5,stroke_width=1)))

            
            label = MathTex("(-3\pi, 0)", color=WHITE, font_size=20).next_to(Dot(axes.c2p(i*pi-3*pi,0)), DOWN + RIGHT, buff=0.2)
            label2 = MathTex("(-2\pi, 0)", color=WHITE, font_size=20).next_to(Dot(axes.c2p(i*pi-3*pi,0)), DOWN + RIGHT, buff=0.2)
            label3 = MathTex("(-\pi, 0)", color=WHITE, font_size=20).next_to(Dot(axes.c2p(i*pi-3*pi,0)), DOWN + RIGHT, buff=0.2)
            label4 = MathTex("(0, 0)", color=WHITE, font_size=20).next_to(Dot(axes.c2p(i*pi-3*pi,0)), DOWN + RIGHT, buff=0.2)
            label5 = MathTex("(\pi, 0)", color=WHITE, font_size=20).next_to(Dot(axes.c2p(i*pi-3*pi,0)), DOWN + RIGHT, buff=0.2)
            label6 = MathTex("(2\pi, 0)", color=WHITE, font_size=20).next_to(Dot(axes.c2p(i*pi-3*pi,0)), DOWN + RIGHT, buff=0.2)
            label_pontos=[label,label2,label3,label4,label5,label6] 
            self.play(Create(label_pontos[i]))

        self.wait(5)
      
      
        self.play(Create(pontosx),run_time=2)
        

        self.play(Create(label_pontos[3]), run_time=0.5)
        self.play(Create(pontosy),run_time=2)
             
        self.wait(5)
        
        
        
       
        
        
    