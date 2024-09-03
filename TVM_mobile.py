from manim import *
from numpy import *

SCALE_FACTOR = 1
tmp_pixel_height = config.pixel_height 
config.pixel_height = config.pixel_width
config.pixel_width=tmp_pixel_height
config.background_color = '#455D3E'
config.frame_height=config.frame_height/SCALE_FACTOR
config.frame_width=config.frame_height*9/16
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width




class TeoremadoVM2(Scene):
    
    def setup(self, add_border=True):
        if add_border:
            self.border=Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=WHITE)
            self.add(self.border)

    def construct(self):
        
        #OBJETOS
       
        axes=Axes(x_range=[0,15],
                  y_range=[0,20],
                  x_length=4,
                  y_length=4,                  
                  stroke_width=0.1).shift(DOWN)
        
       
      
        graph1=axes.plot(lambda x: 0.1*(x-2)**3-2*(x-2)**2+11*(x-2)-4,
                         x_range=[2.39,13],
                         color=WHITE,)
        
       
        pontoA=Dot(axes.c2p(3.28,7),
                   fill_opacity=5,
                   stroke_width=0.5)
        
        pontoB=Dot(axes.c2p(12.61,7),
                   fill_opacity=5,
                   stroke_width=1)
        
        pontoB1=Dot(axes.c2p(8,11.6))
        
        pontoC=Dot(axes.c2p(5.81,14.41),
                   fill_opacity=5,
                   stroke_width=1)
        
        pontoC1=Dot(axes.c2p(5.34,14.16))

        
        pontoD=Dot(axes.c2p(11.52,5.74),
                   fill_opacity=5,
                   stroke_width=1)
        
        
        linhaPontoA=DashedLine(start=axes.c2p(3.28,0),
                               end=axes.c2p(3.28,7))
        
        
        
        linhaPontoB=DashedLine(start=axes.c2p(12.61,0),
                               end=axes.c2p(12.61,7))
        
        linhaPontoB1=DashedLine(start=axes.c2p(8,0),
                               end=axes.c2p(8,11.6))
      
        linhafdeA=DashedLine(start=axes.c2p(0,7),
                             end=axes.c2p(12.61,7))
        
        linhaPontoC=Line(start=axes.c2p(1.97,14.41),
                         end=axes.c2p(9.99,14.41),
                         color=YELLOW)
        
        linhaPontoD=Line(start=axes.c2p(8,5.74),
                         end=axes.c2p(14,5.74),
                         color=YELLOW)
        
        linhaPontoAB=Line(start=pontoA,
                                end=pontoB1,
                                color=YELLOW)
        
        linhaPontoC1=Line(start=axes.c2p(0.70727,9.63985),end=axes.c2p(9.61009,18.31633),color=YELLOW)
        

               
        #Textos


        titulo=Text("Teorema de Rolle", 
                        font_size=24,
                        color=WHITE).shift(3.25*UP)
        titulo2=Text("Teorema do Valor Medio:", 
                        font_size=24,
                        color=WHITE).shift(2.80*UP)
        flinhadec = MathTex(r"f'(c)&=\frac{\triangle y}{\triangle x}\\&=\frac{y-y_o}{x-x_o}\\ &=\frac{f(b)-f(a)}{b-a}",
                            font_size=24).shift(2*UP+LEFT)
        
        axes_label=axes.get_axis_labels(x_label="x",
                                        y_label="y")
        
        pontoFdeA=Text("f(a)=f(b)",font_size=14).next_to(Dot(axes.c2p(8,7),fill_opacity=5,stroke_width=1),DOWN)
        pontoFdeAeB=Text("f(a)≠f(b)",font_size=14).next_to(Dot(axes.c2p(5,7),fill_opacity=5,stroke_width=1),DOWN)
        labelPontoC1=Text("c",font_size=14).next_to(pontoC1,UP)
        


        #Animações


        #TEOREMA DE ROLLE
        self.play(Write(titulo),run_time=2)
        self.play(Write(titulo2),run_time=2)
        self.play(Create(axes),Create(axes_label),run_time=3)
        self.play(Create(graph1))
        self.play(Create(pontoA))
        self.play(Create(pontoB))#10 segundos

        self.play(Create(linhaPontoA),run_time=1.5)
        self.play(Create(linhaPontoB),run_time=1.5)
        self.play(Create(linhafdeA))
        self.play(Write(pontoFdeA)) #15 segundos
        self.wait(3)
        self.play(Flash(pontoA))
        self.play(Flash(pontoB)) #20 segundos
        
        self.play(Create(pontoC))
        self.play(Flash(pontoC))
        self.play(Create(linhaPontoC),run_time=5) #27 segundos

        self.wait(7)
        self.play(Create(pontoD))
        self.play(Flash(pontoD))
        self.play(Create(linhaPontoD))
        self.wait(8) #45 segundos

        #TEOREMA DO VALOR MEDIO
        #ATÉ OS 58 SEGUNDOS PRECISA ESTA O GRAPH2, 2 OUTROS PONTOS 

        #58-1:04: aparecerá o ponto c com as linhas
        #1:04-1:13: Aparecerá a reta que passa por C e depois a reta que passa por AB
        #1:13- até o final: todo grafico descerá 1 unidade e começará o calculo para achar f'(c)
        
        self.play(FadeOut(titulo))      
        self.play(FadeOut(pontoB),FadeOut(linhaPontoB),FadeOut(linhaPontoA))
        self.play(FadeOut(linhafdeA),FadeOut(pontoFdeA))
        self.play(FadeOut(pontoC),FadeOut(linhaPontoC))
        self.play(FadeOut(pontoD),FadeOut(linhaPontoD))#50 segundos
        
        self.play(Create(linhaPontoA))
        self.play(Create(linhaPontoB1))
        self.play(Create(pontoB1))       
        self.wait()
        self.play(Write(pontoFdeAeB))
        self.wait(8)#1:03
        self.play(Create(pontoC1))
        self.play(Write(labelPontoC1))
        self.play(Create(linhaPontoC1))
        self.wait(3)
        self.play(Create(linhaPontoAB))
        self.wait(3)
        
        #####AQUI COMEÇAM OS CALCULOS NA TELA ###########      
        
        grupo=VGroup(axes,graph1,pontoA,pontoB1,linhaPontoAB,pontoC1,linhaPontoC1,axes_label,linhaPontoA,linhaPontoB1,labelPontoC1)
        self.play(grupo.animate.shift(0.75*DOWN),FadeOut(pontoFdeAeB))
        self.play(titulo2.animate.shift(UP))
        self.play(Write(flinhadec),run_time=10)
        self.wait(10)