from manim import *
from numpy import *



class Seno(Scene):
    def construct(self):

        k = ValueTracker(0.0001)


        axes2=Axes(x_range=[-2,2],
                   y_range=[-2*np.pi,2*np.pi],
                   x_length=5,
                   y_length=3,
                   axis_config={'include_tip': False,'include_numbers':True}).shift(1.5*DOWN)
        pontoA=Dot(axes.c2p(np.pi/4,sin(np.pi/4)))
        label_pontoA=Text('A',size=8,color=RED).next_to(pontoA,UP)

        axes=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.5).shift(1.5*UP)
        pontoA1=Dot(axes.c2p(0.7,0.7))

        curva_parametrica=axes.plot_parametric_curve(
            lambda t:[np.sin(-t),np.cos(-t),0],
                   t_range=[3*np.pi/2,7*np.pi/4],
                   color=BLUE)

        curva_parametrica2=axes.plot_parametric_curve(lambda t:[np.sin(t+np.pi/2),np.cos(t+np.pi/2),0],t_range=[0,2*np.pi],color=RED)

        seno=axes2.plot((lambda x: sin(x)), x_range=[-2*np.pi,2*np.pi],color=BLUE)
        


        linha1=Line(start=axes.c2p(0,0),end=axes.c2p(0.7,0.7),color=BLUE)
        linha2=Line(start=axes.c2p(0,0),end=axes.c2p(1,0))
        angle= Angle(linha1,linha2,radius=0.4, other_angle=True)

        
        self.play(Create(axes),Create(axes2))
   
        
        self.play(Create(curva_parametrica2),Create(seno),run_time=3)
        self.play(Create(curva_parametrica))      
        self.play(Create(linha1),Create(angle))

      
       

        self.wait(5)