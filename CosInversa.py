from manim import *
from numpy import *

class CosInversa(Scene):
    def construct(self):
        axes = Axes(x_range=[-3/2*pi,3/2*pi], x_length=10, y_range=[-3,3],y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")
        axes2 = Axes(x_range=[-3,3], x_length=5, y_range=[-3*pi,3*pi],y_length=10)
        
        #OBJETOS
        cossenao= axes.plot(lambda x: cos(x),x_range=[-3/2*pi,3/2*pi],color=RED )
        cosseninho=axes.plot(lambda x: cos(x),x_range=[0,pi],color=RED)
        arccosseno=axes.plot(lambda x: arccos(x),x_range=[-1,1], color=BLUE )
        coseninho_copy=cosseninho.copy()
        line1 = DashedLine(start=axes.c2p(0,-3),end=axes.c2p(0,3))
        line2 = DashedLine(start=axes.c2p(pi,-3),end=axes.c2p(pi,3))
        line3 = DashedLine(start=axes.c2p(-3,-3),end=axes.c2p(2,2))

        #TEXTOS
        inversa=MathTex("\\text{Função Inversa}:", font_size=36, color=WHITE).shift(3.25*UP)
        inversa2=MathTex("\\text{A inversa é espelhada em relação a reta y=x}", font_size=36,color=WHITE).shift(3*DOWN)
        cosseno=MathTex("f(x)=cos(x)").set_color(RED).set_height(0.5).shift(2.5*UP,3*LEFT)
        cosseno_copy=cosseno.copy()
        arcscos=MathTex("f^{-1}(x)=arccos(x)").set_color(BLUE).set_height(0.5).shift(2.5*UP,3*RIGHT)
        domcos= MathTex("D_f=[0,\pi]",color=RED,font_size=28).shift(2*UP+3*LEFT)
        imgcos= MathTex("Im(f)=[-1,1]",color=RED,font_size=28).shift(1.5*UP+3*LEFT)


        domarc= MathTex("D_{f^{-1}}=[-1,1]",color=BLUE,font_size=28).shift(2*UP+3*RIGHT)
        imgarc= MathTex("Im(f^{-1})=[0,\pi]",color=BLUE,font_size=28).shift(1.5*UP+3*RIGHT)

        #PONTOS

        

        #ANIMAÇÃO
        
        self.play(Create(axes),Write(axes_label))
        self.play(Write(cosseno))
        self.add(cosseno_copy)
        self.play(Write(inversa))
        self.play(Create(cossenao))
        self.play(Write(domcos))
        self.play(Write(imgcos))
        self.add(cosseninho)
        
        self.play(Create(line1),Create(line2))
        self.play(FadeOut(cossenao))
        self.wait()
        self.play(FadeOut(line1),FadeOut(line2))
        self.wait()
        self.play(Create(arccosseno))
        self.wait()
        self.play(Transform(cosseno,arcscos))
        self.play(Transform(domcos.copy(),domarc),Transform(imgcos.copy(),imgarc))
        self.play(Create(line3))
        self.wait()
        self.play(Transform(cosseninho,arccosseno),run_time=3)
        
        
        self.play(Write(inversa2))


        self.wait(5)