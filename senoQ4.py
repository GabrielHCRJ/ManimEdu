from manim import *
from numpy import *

class SenoQ4(Scene):  
           
   
   #CRIAR NOVOS PONTOS DIFERENTES NO GRÁFICO E A RESPOSTA CERTA VAI SER A LETRA b
    # A=11*PI/36
    # B=5*PI/6
    # C=7*pi/6
    # D=5PI/3


    def construct(self):
       
        #EIXOS
        axes_graph=Axes(x_range=[0,2*np.pi],
                   y_range=[-1,1],
                   x_length=5,
                   y_length=3,
                   
                   axis_config={'include_tip': False, 'include_ticks': False,}).shift(1.75*DOWN)
        
        axes=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.5).shift(2*UP)
      
        #PONTOS E LABELS

        label_graph0=MathTex("0",color=WHITE,font_size=24).next_to(Dot(axes_graph.c2p(0,0)),0.5*DOWN+0.5*LEFT)
        label_graphpi2=MathTex("\\frac{\\pi}{2}",color=WHITE,font_size=24).next_to(Dot(axes_graph.c2p(np.pi/2,0)),0.5*DOWN)
        label_graphpi=MathTex("\\pi",color=WHITE,font_size=24).next_to(Dot(axes_graph.c2p(np.pi,0)),0.5*DOWN)
        label_graph3pi2=MathTex("\\frac{3\\pi}{2}",color=WHITE,font_size=24).next_to(Dot(axes_graph.c2p(3*np.pi/2,0)),0.5*DOWN)
        label_graph2pi=MathTex("2\\pi",color=WHITE,font_size=24).next_to(Dot(axes_graph.c2p(2*np.pi,0)),0.5*DOWN)

       

        label_circulo0=MathTex('0=2\\pi',color=WHITE,font_size=24).next_to(Dot(axes.c2p(1,0)),0.5*RIGHT)
        label_circulopi2=MathTex('\\frac{\\pi}{2}',color=WHITE,font_size=24).next_to(Dot(axes.c2p(0,1)),0.5*UP)
        label_circulopi=MathTex('\\pi',color=WHITE,font_size=24).next_to(Dot(axes.c2p(-1,0)),0.5*LEFT)
        label_circulo3pi2=MathTex('\\frac{3\\pi}{2}',color=WHITE,font_size=24).next_to(Dot(axes.c2p(0,-1)),0.5*DOWN)
     

        pontoA=Dot(axes_graph.c2p(5/6*np.pi,sin(5/6*np.pi)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelA=MathTex("A", 
                       color=WHITE,
                       font_size=24).next_to(pontoA,
                                             0.25*UP + 0.25*RIGHT,
                                             buff=0.2)
        
        
        pontoB=Dot(axes_graph.c2p(5/4*np.pi,sin(5/4*np.pi)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelB=MathTex("B", 
                       color=WHITE,
                       font_size=24).next_to(pontoB,
                                             0.25*UP + 0.25*RIGHT,
                                             buff=0.2)
        
        pontoC=Dot(axes_graph.c2p(5/3*np.pi,sin(5/3*np.pi)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelC=MathTex("C", 
                       color=WHITE,
                       font_size=24).next_to(pontoC,
                                             0.25*DOWN + 0.25*RIGHT,
                                             buff=0.2)
        
        pontoD=Dot(axes_graph.c2p(2*np.pi,sin(2*np.pi)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelD=MathTex("D", 
                       color=WHITE,
                       font_size=24).next_to(pontoD,
                                             DOWN + RIGHT,
                                             buff=0.2)
        
        label_seno=Text("Seno", color=WHITE,font_size=32).shift(0.5*UP+2*LEFT)
        
        #GRÁFICOS

        
        curva_parametrica=axes.plot_parametric_curve(
            lambda t:[np.cos(t),np.sin(t),0],
                   t_range=[0,5*np.pi/3],
                   color=RED)
        
        curva_parametrica2=axes.plot_parametric_curve(
            lambda t:[np.cos(t),np.sin(t),0],
                    t_range=[0,2*np.pi],
                    color=BLUE)

        seno=axes_graph.plot(
            lambda x: sin(x),
                   x_range=[0,2*np.pi],
                   color=BLUE)
        

        #LINHAS E ANGULO

        linha1=Line(start=axes.c2p(0,0),
                    end=axes.c2p(0.5,-0.87),
                    color=RED)
        
        linha2=Line(start=axes.c2p(0,0),
                    end=axes.c2p(1,0),
                    color=RED)

        angle= Angle(linha1,
                     linha2,
                     radius=0.4,
                     other_angle=True,
                     color=RED)
        
        labelAngle=MathTex("\\frac{5\pi}{3}", 
                       color=WHITE,
                       font_size=24).next_to(angle,
                                            0.25*UP+ 0.25*LEFT,
                                             buff=0.2)

        
        #ANIMAÇÃO
   
        self.play(Create(axes),Create(axes_graph))         
                         
        self.play(Create(curva_parametrica2),Create(seno),run_time=3)
        self.play(Write(label_graph0),Write(label_circulo0))
        self.play(Write(label_graphpi2),Write(label_circulopi2))
        self.play(Write(label_graphpi),Write(label_circulopi))
        self.play(Write(label_graph3pi2),Write(label_circulo3pi2))
        self.play(Write(label_graph2pi))  

        self.play(Write(label_seno)) 
     
        self.play(Create(curva_parametrica))      
        self.play(Create(linha1),Create(linha2),Create(angle),Write(labelAngle))
        self.play(Flash(labelAngle))
        self.play(Create(pontoA),Write(labelA))
        self.play(Create(pontoB),Write(labelB))
        self.play(Create(pontoC),Write(labelC))
        self.play(Create(pontoD),Write(labelD))

      
       

        self.wait(10)