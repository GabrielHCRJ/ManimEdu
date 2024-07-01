from manim import *
from numpy import *

class ITF(Scene):  
          
#     Principais cores:
# - #61acc9 - azul
# - #fd5151 vermelho
# - #fffdec fundo(branco?)

# Cores secundárias:
# - #004aad
# - #d21616
# - #ffffff
# - #000000

#REVERTER AS CORES
#TRABALHAR COM A CAMERA

    def construct(self):
        self.camera.background_color= '#fffdec'

        ITFtexto=Tex("Identidade Trigonométrica Fundamental", color='#61acc9',font_size=48).shift(3*UP).set_stroke(width=2)
        self.play(Write(ITFtexto),run_time=1)

        ITF=MathTex('sen^2(x)+cos^2(x)=1',color='#61acc9',font_size=48).set_stroke(width=2)

        self.play(Write(ITF))
        self.play(FadeOut(ITFtexto),run_time=1)
        self.play(ITF.animate.shift(3*UP))
        
        

        axes=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.75).shift(1.75*DOWN).set_color('#61acc9')
        
        self.play(Create(axes))

        curva_parametrica=axes.plot_parametric_curve(
            lambda t:[np.cos(t),np.sin(t),0],
                   t_range=[0,2*np.pi],
                   color=RED_A)
        
        self.play(Create(curva_parametrica))

        hip=Line(start=axes.c2p(0,0),
                    end=axes.c2p(0.7,0.7),
                    color=RED_E)
        
        hipcopy=hip.copy()

        hipcopy2=hip.copy()

        catadj=Line(start=axes.c2p(0,0),
                    end=axes.c2p(0.7,0),
                    color=RED_E)
        
        catadjcopy=catadj.copy()
        
        catop=Line(start=axes.c2p(0.7,0),
                    end=axes.c2p(0.7,0.7),
                    color=RED_E)
        
        catopcopy=catop.copy()
        
     
        
        self.play(Create(catop),Create(catadj),Create(hip))


        seno=MathTex('sen(x)=\\frac{CO}{Hip}',color='#61acc9',font_size=32).shift(2*UP+2.25*RIGHT).set_stroke(width=2)
        senocopy=seno.copy()
        self.play(Transform(catadjcopy,seno),Transform(hipcopy,seno),run_time=2)
        
        

        cosseno=MathTex('cos(x)=\\frac{CA}{Hip}',color='#61acc9',font_size=32).shift(0.75*UP+2.25*RIGHT).set_stroke(width=2)
        cossenocopy=cosseno.copy()
        
        self.play(Transform(catopcopy,cosseno),Transform(hipcopy2,cosseno),run_time=2)


        self.play(FadeOut(catadj),FadeOut(catop),FadeOut(hip),FadeOut(curva_parametrica),FadeOut(axes))

        ITF2=MathTex("\\left(\\frac{CO}{Hip}\\right)^2+\\left(\\frac{CA}{Hip}\\right)^2=",color='#61acc9',font_size=32).shift(2*UP+LEFT).set_stroke(width=2)

        
        self.play(Transform(senocopy,ITF2),Transform(cossenocopy,ITF2))

        ITF3=MathTex("\\frac{CO^2}{Hip^2}+\\frac{CA^2}{Hip^2}=",color='#61acc9',font_size=32).next_to(ITF2,1.25*DOWN).set_stroke(width=2)
        self.play(Write(ITF3))

        ITF4=MathTex("\\frac{CO^2+CA^2}{Hip^2}=",color='#61acc9',font_size=32).next_to(ITF3,1.25*DOWN).set_stroke(width=2)
        self.play(Write(ITF4))

        # Definindo os vértices do triângulo retângulo
        A = np.array([0, 0, 0])  # Vértice no ponto (0, 0)
        B = np.array([4, 0, 0])  # Vértice no ponto (4, 0)
        C = np.array([4, 3, 0])  # Vértice no ponto (4, 3)

        # Criando o triângulo retângulo com os vértices A, B e C
        
        
        right_triangle = Polygon(A, B, C, color='#fd5151').scale(0.5).shift(2.75*DOWN+RIGHT)
        teorema=MathTex('Teorema\\ de\\ Pitagoras\\',color='#61acc9',font_size=32).next_to(right_triangle,UP).set_stroke(width=2)
        self.play(Write(teorema))

        # Adicionando o triângulo à cena
        self.play(Create(right_triangle))
        pitagoras=MathTex('CO^2+CA^2=Hip^2',color='#61acc9',font_size=24).next_to(right_triangle,DOWN).set_stroke(width=2)
        self.play(Write(pitagoras))

        ITF5=MathTex("\\frac{Hip^2}{Hip^2}=1",color='#61acc9',font_size=32).next_to(ITF4,1.25*DOWN).set_stroke(width=2)
        self.play(Write(ITF5))
        qed_symbol = MathTex(r'\blacksquare', font_size=8,color='#61acc9').next_to(ITF5, DOWN+RIGHT)

        self.play(Write(qed_symbol))


       

            
      
      
       

        self.wait(10)