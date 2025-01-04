from manim import *
from numpy import *

class SenoQ1(Scene):  
    
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
     

        pontoA=Dot(axes_graph.c2p(np.pi/4,sin(np.pi/4)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        
        
        pontoD=Dot(axes_graph.c2p(4*np.pi/3,sin(4*np.pi/3)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        pontoB=Dot(axes_graph.c2p(np.pi/2,sin(np.pi/2)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
    
        pontoC=Dot(axes_graph.c2p(np.pi,sin(np.pi)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
    
        
        #GRÁFICOS

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
   
        self.add(axes,axes_graph)         
                         
        self.add(curva_parametrica2,seno)
        self.add(label_graph0,label_circulo0)
        self.add(label_graphpi2,label_circulopi2)
        self.add(label_graphpi,label_circulopi)
        self.add(label_graph3pi2,label_circulo3pi2)
        self.add(label_graph2pi)  

        # self.add(label_seno) 
     
        self.add(curva_parametrica)      
        self.add(linha1,linha2,angle,labelAngle)        

        self.add(pontoA)
        self.add(pontoB)
        self.add(pontoC)
        self.add(pontoD)

        def respostas(label,ponto,x):
            labelA=MathTex(label, #O QUE VAI ESTA ESCRITO DO LADO DO PONTO
                       color=WHITE,
                       font_size=32).next_to(ponto, # QUAL O PONTO DA RESPOSTA?
                                             0.5*DOWN +10*RIGHT,
                                             buff=0.2) 
            
            linhaRx=DashedLine(start=axes_graph.c2p(x,0),
                        end=axes_graph.c2p(x,sin(x)),
                        color=WHITE)
            linhaRy=DashedLine(start=axes_graph.c2p(0,sin(x)),
                        end=axes_graph.c2p(x,sin(x)),
                        color=WHITE)
            
            self.add(labelA)
            self.add(linhaRx,linhaRy)

        respostas('A=(\\frac{\\pi}{4},sen(\\frac{\\pi}{4}))',pontoA,pi/4)

      
       

        self.wait(10)