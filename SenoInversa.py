from manim import *
from numpy import *

class SenoInversa(Scene):
    def construct(self):
        axes = Axes(x_range=[-2*pi,2*pi], x_length=10, y_range=[-3,3], y_length=5, axis_config={'include_tip':True}).set_color('BLUE')
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")
        
        
        #OBJETOS
        senao= axes.plot(lambda x: sin(x),x_range=[-2*pi,2*pi],color=YELLOW )
        seninho=axes.plot(lambda x: sin(x),x_range=[-pi/2,pi/2],color=YELLOW)
        arcsen=axes.plot(lambda x: arcsin(x),x_range=[-1,1], color=BLUE )
        seninho_copy=seninho.copy()
        line1 = DashedLine(start=axes.c2p(-pi/2,-3),end=axes.c2p(-pi/2,3),color=RED)
        line2 = DashedLine(start=axes.c2p(pi/2,-3),end=axes.c2p(pi/2,3),color=RED)
        line3 = DashedLine(start=axes.c2p(-3,-3),end=axes.c2p(2,2),color=RED)

        #TEXTOS
        inversa=MathTex("\\text{Função Inversa}:", font_size=36, color=WHITE).shift(3.25*UP)
        inversa2=MathTex("\\text{A inversa é espelhada em relação a reta y=x}", font_size=36,color=WHITE).shift(3*DOWN)
        seno=MathTex("f(x)=sen(x)").set_color(YELLOW).set_height(0.5).shift(2.5*UP,3*LEFT)
        seno_copy=seno.copy()
        arcseno=MathTex("f^{-1}(x)=arcsen(x)").set_color(BLUE).set_height(0.5).shift(2.5*UP,3*RIGHT)
        domseno= MathTex("D_f=[\\frac{-\pi}{2},\\frac{\pi}{2}]",color=YELLOW,font_size=28).shift(2*UP+3*LEFT)
        imgseno= MathTex("Im(f)=[-1,1]",color=YELLOW,font_size=28).shift(1.5*UP+3*LEFT)


        domarc= MathTex("D_{f^{-1}}=[-1,1]",color=BLUE,font_size=28).shift(2*UP+3*RIGHT)
        imgarc= MathTex("Im(f^{-1})=[\\frac{-\pi}{2},\\frac{\pi}{2}]",color=BLUE,font_size=28).shift(1.5*UP+3*RIGHT)

               

        #ANIMAÇÃO
        
        self.play(Create(axes),Write(axes_label))
        self.play(Write(seno))
        self.add(seno_copy)
        self.play(Write(inversa))
        self.play(Create(senao),run_time=3)
        self.play(Write(domseno))
        self.play(Write(imgseno))
        self.add(seninho)
        
        self.play(Create(line1),Create(line2))
        self.play(FadeOut(senao))
        self.wait()
        self.play(FadeOut(line1),FadeOut(line2))
        self.wait()
        self.play(Create(arcsen))
        self.wait()
        self.play(Transform(domseno.copy(),domarc),Transform(imgseno.copy(),imgarc))
        self.wait(2)
        self.play(Transform(seno,arcseno))        
        self.play(Create(line3))
        self.wait()
        self.play(Transform(seninho,arcsen),run_time=3)
        self.play(FadeOut(line3))
        
        self.play(Write(inversa2))


        self.wait(5)