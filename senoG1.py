from manim import *
from numpy import *

class SenoG1(Scene):     
     
    def construct(self):
       
        #EIXOS
        axes_graph=Axes(x_range=[0,2*np.pi],
                   y_range=[-1,1],
                   x_length=5,
                   y_length=3,
                   
                   axis_config={'include_tip': False, 'include_ticks': False,}).shift(2*UP)
        
        axes=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.5).shift(1.75*DOWN)
      
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
            
        label_seno=Text("Seno", color=WHITE,font_size=32).shift(0.5*UP+2*LEFT)
        
        #GRÁFICOS
        A = axes.c2p(0, 0)         # Ponto A (0, 0)
        B = axes.c2p(np.pi / 4, 0) # Ponto B (pi/4, 0)
        C = axes.c2p(np.pi / 4, np.pi / 4) # Ponto C (pi/4, 1)

        # Criando o triângulo retângulo com os pontos A, B e C
        right_triangle = Polygon(A, B, C, color=BLUE)

        # Adicionando o triângulo à cena
        self.play(Create(right_triangle))

        curva_parametrica=axes.plot_parametric_curve(
            lambda t:[np.cos(t),np.sin(t),0],
                   t_range=[0,np.pi/4],
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
                    end=axes.c2p(0.7,0.7),
                    color=RED)
        
        linha2=Line(start=axes.c2p(0,0),
                    end=axes.c2p(1,0),
                    color=RED)

        angle= Angle(linha1,
                     linha2,
                     radius=0.4,
                     other_angle=True,
                     color=RED)
        
        labelAngle=MathTex("\\frac{\pi}{4}", 
                       color=WHITE,
                       font_size=24).next_to(angle,
                                             DOWN + RIGHT,
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
      
       

        self.wait(10)