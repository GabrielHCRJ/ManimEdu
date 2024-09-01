from manim import *
from numpy import *


class IdentidadeTrigonometricaFundamental(MovingCameraScene):  
          
#     Principais cores:
# - #61acc9 - azul
# - #fd5151 vermelho
# - #fffdec fundo(branco?)

# Cores secundárias:
# - #004aad
# - #d21616
# - #ffffff
# - #000000


  

    def construct(self):
        COR_TEXTOS=BLUE
        COR_AXES=''
        COR_TRIANGULO=RED_E


        ITFtexto=Tex("Identidade Trigonométrica Fundamental", color=COR_TEXTOS,font_size=48).shift(3*UP).set_stroke(width=2)
        self.play(Write(ITFtexto),run_time=1)

        self.camera.frame.save_state()
        ITF=MathTex('sen^2(x)+cos^2(x)=1',color=COR_TEXTOS,font_size=56).set_stroke(width=2)
        ITFcopy=ITF.copy().set_stroke(width=15, opacity=0.2).set_color(COR_TEXTOS)

        self.play(Write(ITF),Write(ITFcopy))
        self.play(FadeOut(ITFtexto),run_time=1)
        self.play(ITF.animate.shift(3.25*UP),ITFcopy.animate.shift(3.25*UP))
        
        

        axes=Axes(x_range=[-1,1],
                  y_range=[-1,1],
                  x_length=5,
                  y_length=5,
                  axis_config={'include_tip': False}).scale(0.75).shift(1.75*DOWN).set_color(COR_TEXTOS)
        
        self.play(Create(axes))
        self.play(self.camera.frame.animate.set(width=axes.width *2).move_to(axes))

        curva_parametrica=axes.plot_parametric_curve(
            lambda t:[np.cos(t),np.sin(t),0],
                   t_range=[0,2*np.pi],
                   color=RED_A)
        
        self.play(Create(curva_parametrica))

        hip=Line(start=axes.c2p(0,0),
                    end=axes.c2p(0.7,0.7),
                    color=COR_TRIANGULO)
        
        hipcopy=hip.copy()

        hipcopy2=hip.copy()

        catadj=Line(start=axes.c2p(0,0),
                    end=axes.c2p(0.7,0),
                    color=COR_TRIANGULO)
        
        catadjcopy=catadj.copy()

        
        
        catop=Line(start=axes.c2p(0.7,0),
                    end=axes.c2p(0.7,0.7),
                    color=COR_TRIANGULO)
        
        
        catopcopy=catop.copy()
        
     
       
        self.play(Create(catop),Create(catadj),Create(hip))

        catadj_label=Text('CA',font_size=16,color=WHITE).next_to(catadj,DOWN)
        catop_label=Text('CO',font_size=16,color=WHITE).next_to(catop,0.25*RIGHT)
        hip_label=Text('Hip',font_size=16,color=WHITE).next_to(catadj,3.5*UP)

        self.play(Write(catadj_label))
        self.wait()
        self.play(Write(catop_label))
        self.wait()
        self.play(Write(hip_label))
        self.wait()
        

        seno=MathTex('sen(x)=\\frac{CO}{Hip}',color=COR_TEXTOS,font_size=32).shift(2*UP+2.25*RIGHT).set_stroke(width=2)
        senocopy=seno.copy()
        self.play(Transform(catadjcopy,seno),Transform(hipcopy,seno),Restore(self.camera.frame),run_time=2)
        
        

        cosseno=MathTex('cos(x)=\\frac{CA}{Hip}',color=COR_TEXTOS,font_size=32).shift(0.75*UP+2.25*RIGHT).set_stroke(width=2)
        cossenocopy=cosseno.copy()
        ids=VGroup(seno,cosseno)
        caixa = SurroundingRectangle(ids, buff=0.5,color=COR_TEXTOS,corner_radius=0.2).scale(0.75) 
        
        self.play(Transform(catopcopy,cosseno),Transform(hipcopy2,cosseno),run_time=2)
        self.play(Create(caixa))

        self.play(FadeOut(catadj),FadeOut(catop),FadeOut(hip),FadeOut(curva_parametrica),FadeOut(axes),FadeOut(catadj_label),FadeOut(catop_label),FadeOut(hip_label))

        ITF2=MathTex("\\left(\\frac{CO}{Hip}\\right)^2+\\left(\\frac{CA}{Hip}\\right)^2=",color=COR_TEXTOS,font_size=32).shift(2*UP+LEFT).set_stroke(width=2)

        
        self.play(Transform(senocopy,ITF2),Transform(cossenocopy,ITF2))

        ITF3=MathTex("\\frac{CO^2}{Hip^2}+\\frac{CA^2}{Hip^2}=",color=COR_TEXTOS,font_size=32).next_to(ITF2,1.25*DOWN).set_stroke(width=2)
        self.play(Write(ITF3))

        ITF4=MathTex("\\frac{CO^2+CA^2}{Hip^2}=",color=COR_TEXTOS,font_size=32).next_to(ITF3,1.25*DOWN).set_stroke(width=2)
        self.play(Write(ITF4))
        self.wait(2)

        # Definindo os vértices do triângulo retângulo
        A = np.array([0, 0, 0])  # Vértice no ponto (0, 0)
        B = np.array([4, 0, 0])  # Vértice no ponto (4, 0)
        C = np.array([4, 3, 0])  # Vértice no ponto (4, 3)

        # Criando o triângulo retângulo com os vértices A, B e C
        
        
        right_triangle = Polygon(A, B, C, color='#fd5151').scale(0.5).shift(2.75*DOWN+RIGHT)
        teorema=MathTex('Teorema\\ de\\ Pitagoras\\',color=COR_TEXTOS,font_size=32).next_to(right_triangle,UP).set_stroke(width=2)
        self.play(Write(teorema))

        # Adicionando o triângulo à cena
        

        self.play(Create(right_triangle))
        self.play(self.camera.frame.animate.set(width=right_triangle.width *2,height=right_triangle.height*2).move_to(right_triangle))
        pitagoras=MathTex('CO^2+CA^2=Hip^2',color=COR_TEXTOS,font_size=24).next_to(right_triangle,DOWN).set_stroke(width=2)
        self.play(Write(pitagoras))
        self.wait(0)
        self.play(Restore(self.camera.frame))
        self.play(self.camera.frame.animate.set(width=ITF4.width*2).move_to(ITF4))
        self.wait()
        ITF5=MathTex("\\frac{Hip^2}{Hip^2}=1",color=COR_TEXTOS,font_size=32).next_to(ITF4,1.25*DOWN).set_stroke(width=2)
        ITF4copy=ITF4.copy()
        self.play(Transform(ITF4copy,ITF5),self.camera.frame.animate.set(width=ITF5.width*2,height=ITF5.height*2).move_to(ITF5))
        qed_symbol = MathTex(r'\blacksquare', font_size=8,color=COR_TEXTOS).next_to(ITF5, DOWN+RIGHT)

        self.play(Write(qed_symbol))
        self.play(Restore(self.camera.frame))
        self.play(Flash(qed_symbol))


       

            
      
      
       

        self.wait(10)