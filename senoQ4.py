from manim import *
from numpy import *



class SenoQ4(Scene):
    
    def construct(self):

    
        axes2=Axes(x_range=[-2*np.pi,2*np.pi],
                   y_range=[-2,2],
                   x_length=5,
                   y_length=3,
                   axis_config={'include_tip': False, 'include_ticks': True,}).shift(1.5*DOWN)

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
        

        curva_parametrica=axes.plot_parametric_curve(
            lambda t:[np.sin(t),np.cos(t),0],
                   t_range=[5*np.pi/2,11*np.pi/4],
                   color=RED)

        curva_parametrica2=axes.plot_parametric_curve(
            lambda t:[np.sin(t+np.pi/2),
                      np.cos(t+np.pi/2),0],
                      t_range=[0,2*np.pi],
                      color=BLUE)

        seno=axes2.plot(
            lambda x:
                    sin(x),
                    x_range=[-2*np.pi,
                             2*np.pi],
                             color=BLUE)
        
        linha1=Line(
                    start=axes.c2p(0,0),
                    end=axes.c2p(0.7,-0.7),
                    color=RED)
        
        linha2=Line(
                    start=axes.c2p(0,0),
                    end=axes.c2p(1,0))

        angle= Angle(linha2,
                     linha1,
                     radius=0.4,
                     other_angle=True,
                     color=RED)
        
        labelAngle=MathTex("\\frac{-\pi}{4}", 
                       color=WHITE,
                       font_size=24).next_to(angle,
                                             DOWN + RIGHT,
                                             buff=0.2)

        
        self.play(Create(axes),Create(axes2))
   
        
        self.play(Create(curva_parametrica2),Create(seno),run_time=3)
        
        self.play(Create(curva_parametrica))      
        self.play(Create(linha1),Create(angle),Write(labelAngle))
        self.play(Create(pontoA),Write(labelA))
        self.play(Create(pontoB),Write(labelB))
        self.play(Create(pontoC),Write(labelC))
        self.play(Create(pontoD),Write(labelD))

      
       

        self.wait(5)