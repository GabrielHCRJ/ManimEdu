from manim import *
from numpy import *

class TgInversa(Scene):
    def construct(self):
        axes = Axes(x_range=[-3*pi,3*pi], x_length=10, y_range=[-10,10],y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axes_label=axes.get_axis_labels(x_label="x",y_label="y")
     
        
        #TG
        tg1 = axes.plot((lambda x: tan(x)), x_range=[-3*pi,(-5*pi/2)-0.10], color=RED, stroke_width=5)
        tg2 = axes.plot((lambda x: tan(x)), x_range=[(-5*pi/2)+0.10,(-3*pi/2)-0.10], color=RED, stroke_width=5)
        tg3 = axes.plot((lambda x: tan(x)), x_range=[(-3*pi/2)+0.10,(-pi/2)-0.10], color=RED, stroke_width=5)
        tg4 = axes.plot((lambda x: tan(x)), x_range=[(-pi/2)+0.10,(pi/2)-0.10], color=RED, stroke_width=5)
        tg5 = axes.plot((lambda x: tan(x)), x_range=[pi/2+0.10,((3*pi)/2)-0.10], color=RED, stroke_width=5)
        tg6 = axes.plot((lambda x: tan(x)), x_range=[(3*pi/2)+0.10,(5*pi/2)-0.10], color=RED, stroke_width=5)
        tg7 = axes.plot((lambda x: tan(x)), x_range=[(5*pi/2)+0.10,3*pi], color=RED, stroke_width=5)


        tginho=axes.plot(lambda x: tan(x),x_range=[-pi/2+0.1,pi/2-0.10],color=RED)

        arctg=axes.plot(lambda x: arctan(x),x_range=[-3*pi,3*pi], color=BLUE )
        tginho_copy=tginho.copy()
        line1 = DashedLine(start=axes.c2p(-pi/2,-10),end=axes.c2p(-pi/2,10))
        line2 = DashedLine(start=axes.c2p(pi/2,-10),end=axes.c2p(pi/2,10))
        line3 = DashedLine(start=axes.c2p(-10,-10),end=axes.c2p(5,5))

        #TEXTOS
        inversa=MathTex("\\text{Função Inversa}:", font_size=36, color=WHITE).shift(3.25*UP)
        inversa2=MathTex("\\text{A inversa é espelhada em relação a reta y=x}", font_size=36,color=WHITE).shift(3*DOWN)
        tangente=MathTex("f(x)=tg(x)").set_color(RED).set_height(0.5).shift(3*UP,3*LEFT)
        tangente_copy=tangente.copy()
        arctangente=MathTex("f^{-1}(x)=arctg(x)").set_color(BLUE).set_height(0.5).shift(3*UP,3*RIGHT)
        domtg= MathTex("D=[\\frac{-\pi}{2},\\frac{\pi}{2}]",color=RED,font_size=28).shift(2*UP+3*LEFT)
        imgtg= MathTex("Im(f)=\mathbb{R}",color=RED,font_size=28).shift(1.5*UP+3*LEFT)


        domarc= MathTex("D=\mathbb{R}",color=BLUE,font_size=28).shift(2*UP+3*RIGHT)
        imgarc= MathTex("Im(f^{-1})=[\\frac{-\pi}{2},\\frac{\pi}{2}]",color=BLUE,font_size=28).shift(1.5*UP+3*RIGHT)

        #PONTOS

        

        #ANIMAÇÃO
        
        self.play(Create(axes),Write(axes_label))
        self.play(Write(tangente))
        self.add(tangente_copy)
        self.play(Write(inversa))
        self.play(Create(tg1))
        self.play(Create(tg2))
        self.play(Create(tg3))
        self.play(Create(tg4))
        self.play(Create(tg5))
        self.play(Create(tg6))
        self.play(Create(tg7))
        self.add(tginho)
        
        
        
        self.play(Create(line1),Create(line2))
        self.play(FadeOut(tg1))
        self.play(FadeOut(tg2))
        self.play(FadeOut(tg3))
        self.play(FadeOut(tg4))
        self.play(FadeOut(tg5))
        self.play(FadeOut(tg6))
        self.play(FadeOut(tg7))
        self.play(Write(domtg))
        self.play(Write(imgtg))
        self.wait()
        self.play(FadeOut(line1),FadeOut(line2))
        self.play(Create(line3))
        self.wait()
        self.play(Create(arctg),run_time=3)
        self.wait()
        self.play(Transform(tangente,arctangente))
        self.play(Transform(domtg.copy(),domarc),Transform(imgtg.copy(),imgarc))
        
        self.wait()
        self.play(Transform(tginho,arctg),run_time=3)
        
        
        self.play(Write(inversa2))


        self.wait(5)