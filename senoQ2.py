from manim import *
from numpy import *



class SenoQ2(Scene):
    CONFIG = {
        'x_min' : -0.5,
        'x_max':2.1*pi,
        "x_tick_frequency": pi/4,
        "x_leftmost_tick": pi/4,
        'y_min': -1.5,
        'y_max':1.5,
        "y_tick_frequency": 0.5,
        'graph_origin': 4*LEFT,
        'axes_color': BLUE
    }

    def construct(self):


        # o ponto pi/4,pi/2,3pi/2,pi
    
        axes2=Axes(x_range=[-2*np.pi,2*np.pi],
                   y_range=[-2,2],
                   x_length=5,
                   y_length=3,
                   axis_config={'include_tip': False, 'include_ticks': True,}).shift(1.5*DOWN)

      
       # label_pontoA=Text('A',size=8,color=RED).next_to(pontoA,UP)

        axes=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.5).shift(2*UP)
      
        #PONTOS E LABELS
        pontoA=Dot(axes2.c2p(np.pi/4,sin(np.pi/4)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelA=MathTex("A", 
                       color=WHITE,
                       font_size=24).next_to(pontoA,
                                             DOWN + RIGHT,
                                             buff=0.2)
        pontoB=Dot(axes2.c2p(-np.pi/4,sin(-np.pi/4)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelB=MathTex("B", 
                       color=WHITE,
                       font_size=24).next_to(pontoB,
                                             DOWN + LEFT,
                                             buff=0.2)
        pontoC=Dot(axes2.c2p(np.pi/2,sin(np.pi/2)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelC=MathTex("C", 
                       color=WHITE,
                       font_size=24).next_to(pontoC,
                                             UP + RIGHT,
                                             buff=0.2)
        pontoD=Dot(axes2.c2p(np.pi,sin(np.pi)),
                   color=RED,
                   fill_opacity=5,
                   stroke_width=1)
        
        labelD=MathTex("D", 
                       color=WHITE,
                       font_size=24).next_to(pontoD,
                                             DOWN + RIGHT,
                                             buff=0.2)
        

        #pontoA1=Dot(axes.c2p(0.7,0.7))

        curva_parametrica=axes.plot_parametric_curve(
            lambda t:[np.sin(-t),np.cos(-t),0],
                   t_range=[3*np.pi/2,9*np.pi/4],
                   color=RED)

        curva_parametrica2=axes.plot_parametric_curve(
            lambda t:[np.sin(t+np.pi/2),
                      np.cos(t+np.pi/2),0],
                      t_range=[0,2*np.pi],
                      color=BLUE)

        seno=axes2.plot((lambda x: sin(x)), x_range=[-2*np.pi,2*np.pi],color=BLUE)
        


        linha1=Line(start=axes.c2p(0,0),end=axes.c2p(-0.7,0.7),color=RED)
        linha2=Line(start=axes.c2p(0,0),end=axes.c2p(1,0),color=RED)

        angle= Angle(linha1,
                     linha2,
                     radius=0.4,
                     other_angle=True,
                     color=RED)
        
        labelAngle=MathTex("\\frac{3\pi}{4}", 
                       color=WHITE,
                       font_size=24).next_to(angle,
                                             0.5*UP + 0.5*RIGHT,
                                             buff=0.2)

        
        self.play(Create(axes),Create(axes2))
   
        
        self.play(Create(curva_parametrica2),Create(seno),run_time=3)
        
        self.play(Create(curva_parametrica))      
        self.play(Create(linha1),Create(linha2),Create(angle),Write(labelAngle))
        self.play(Create(pontoA),Write(labelA))
        self.play(Create(pontoB),Write(labelB))
        self.play(Create(pontoC),Write(labelC))
        self.play(Create(pontoD),Write(labelD))

      
       

        self.wait(5)