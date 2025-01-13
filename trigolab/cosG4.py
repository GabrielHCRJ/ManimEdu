from manim import *
from numpy import *

class CosG4(Scene):     
     
    def construct(self):
       
        #EIXOS
        axes_graph=Axes(x_range=[0,2*np.pi],
                   y_range=[-1,1],
                   x_length=5,
                   y_length=3,
                   
                   axis_config={'include_tip': False, 'include_ticks': False,}).shift(2*UP)
        
     
        axesB=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.5).shift(1.75*DOWN)
        axesC=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.5).shift(1.75*DOWN)
        axesD=Axes(x_range=[-1,1],
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

        #CIRCULO A 
        axesA=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.5).shift(1.75*DOWN)
        
        label_circulo0A=MathTex('2\\pi',color=WHITE,font_size=24).next_to(Dot(axesA.c2p(1,0)),0.5*RIGHT)
        label_circulopi2A=MathTex('\\frac{\\pi}{2}',color=WHITE,font_size=24).next_to(Dot(axesA.c2p(0,1)),0.5*UP)
        label_circulopiA=MathTex('\\pi',color=WHITE,font_size=24).next_to(Dot(axesA.c2p(-1,0)),0.5*LEFT)
        label_circulo3pi2A=MathTex('\\frac{3\\pi}{2}',color=WHITE,font_size=24).next_to(Dot(axesA.c2p(0,-1)),0.5*DOWN)
        
        curva_parametricaA=axesA.plot_parametric_curve(
            lambda t:[np.cos(t),np.sin(t),0],
                    t_range=[0,2*np.
                    pi],
                    color=BLUE)
        curva_parametricaAR=axesA.plot_parametric_curve(
            lambda t:[np.cos(t),np.sin(t),0],
                   t_range=[0,7*pi/6],
                   color=RED)
        

        linha1A=Line(start=axesA.c2p(0,0),
                    end=axesA.c2p(-0.87,-0.5),
                    color=RED)
        
        linha2A=Line(start=axesA.c2p(0,0),
                    end=axesA.c2p(1,0),
                    color=RED)

        angleA= Angle(linha1A,
                     linha2A,
                     radius=0.4,
                     other_angle=True,
                     color=RED)

        label_ponto=MathTex("A",color=WHITE,font_size=32).next_to(linha1A,0.5*UP)
        borda = SurroundingRectangle(
            curva_parametricaA,
            color=YELLOW,
            corner_radius=0.4)
        self.add(borda)
        
        circuloA=VGroup(borda,label_ponto,linha1A,linha2A,angleA,axesA,label_circulo0A,label_circulopi2A,label_circulopiA,label_circulo3pi2A,curva_parametricaA,curva_parametricaAR)

        def circuloB(right,up,left,down,angulo,linhax,linhay,tag,border=BLACK):
            axesA=Axes(x_range=[-1,1],
                    y_range=[-1,1],
                    x_length=5,
                    y_length=5,
                    axis_config={'include_tip': False}).scale(0.5).shift(1.75*DOWN)
            
            label_circulo0A=MathTex('2\\pi',color=WHITE,font_size=24).next_to(Dot(axesA.c2p(1,0)),0.5*RIGHT)
            label_circulopi2A=MathTex('\\frac{\\pi}{2}',color=WHITE,font_size=24).next_to(Dot(axesA.c2p(0,1)),0.5*UP)
            label_circulopiA=MathTex('\\pi',color=WHITE,font_size=24).next_to(Dot(axesA.c2p(-1,0)),0.5*LEFT)
            label_circulo3pi2A=MathTex('\\frac{3\\pi}{2}',color=WHITE,font_size=24).next_to(Dot(axesA.c2p(0,-1)),0.5*DOWN)
            
            curva_parametricaA=axesA.plot_parametric_curve(
                lambda t:[np.cos(t),np.sin(t),0],
                        t_range=[0,2*np.
                        pi],
                        color=BLUE)
            curva_parametricaAR=axesA.plot_parametric_curve(
                lambda t:[np.cos(t),np.sin(t),0],
                    t_range=[0,angulo],
                    color=RED)
            linha1A=Line(start=axesA.c2p(0,0),
                        end=axesA.c2p(linhax,linhay),
                        color=RED)
            
            linha2A=Line(start=axesA.c2p(0,0),
                        end=axesA.c2p(1,0),
                        color=RED)

            angleA= Angle(linha1A,
                        linha2A,
                        radius=0.4,
                        other_angle=True,
                        color=RED)
            
          
            label_ponto=Tex(tag,color=WHITE,font_size=24).next_to(linha1A,1*DOWN)
            borda = SurroundingRectangle(
            curva_parametricaA,
            color=border,
            corner_radius=0.4)
            self.add(borda)
            circuloA=VGroup(borda,label_ponto,linha1A,linha2A,angleA,axesA,label_circulo0A,label_circulopi2A,label_circulopiA,label_circulo3pi2A,curva_parametricaA,curva_parametricaAR)
            self.play(circuloA.animate.scale(0.5).shift(right*RIGHT+up*UP+left*LEFT+down*DOWN))
                        
        cosseno=axes_graph.plot(
        lambda x: cos(x),
                x_range=[0,2*np.pi],
                color=BLUE)
        def graficoAngulo(funcao,angulo,valor):
            graficoR=axes_graph.plot(
                funcao,
                    x_range=[0,angulo],
                    color=RED)
            ponto=Dot(axes_graph.c2p(angulo,cos(angulo)),
                color=RED,
                fill_opacity=5,
                stroke_width=1)
            
            label=MathTex(valor,color=WHITE,font_size=24).next_to(ponto,0.5*RIGHT)
            self.play(Create(graficoR))
            self.play(Create(ponto))
            self.play(Create(label))
            # self.play(Create(ponto),Create(label_ponto))

        #ANIMAÇÃO
   
        self.play(Create(axesA),Create(axes_graph))         
                         
        self.play(Create(curva_parametricaA),Create(cosseno),run_time=3)
        self.play(Write(label_graph0),Write(label_circulo0A))
        self.play(Write(label_graphpi2),Write(label_circulopi2A))
        self.play(Write(label_graphpi),Write(label_circulopiA))
        self.play(Write(label_graph3pi2),Write(label_circulo3pi2A))
        self.play(Write(label_graph2pi))  
        graficoAngulo(lambda x: cos(x),7*pi/6,'\\frac{7\\pi}{6}')
        self.play(Create(curva_parametricaAR))
        self.play(Create(linha1A),Create(linha2A),Create(angleA))
        self.play(Create(label_ponto))
  
        self.wait()
      
        self.play(circuloA.animate.scale(0.5).shift(-2*RIGHT+UP))
        
        circuloB(2,1,0,0,3*pi/4,-0.71,0.71,'B')
        circuloB(-2,-1,0,0,pi/4,0.7,0.7,'C')
        circuloB(2,-1,0,0,5*pi/3,0.5,-0.87,'D')
    

       

        self.wait(10)