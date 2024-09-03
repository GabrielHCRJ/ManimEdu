from manim import *
from numpy import *
##COMO FAÇO O PONTO GIRAR JUNTO COM A FUNÇÃO?##
class CosSimetria(Scene):
    def construct(self):
        
        axes=Axes(x_range=[-10,10],x_length=10,y_range=[-3,3],y_length=5,axis_config={'include_tip':True}).set_color('BLUE')
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")

        graph=axes.plot((lambda x: cos(x)), x_range=[-10,10], stroke_width=7, color=RED)
        graph1=axes.plot(lambda x: cos(x), x_range=[-10,0], color=RED)
        graph2=axes.plot(lambda x: cos(x), x_range=[0,10], color=RED)
        simetria=MathTex("Simetria:",font_size=36).shift(3.25*UP)
    
 

        resposta=Text("Função par:",font_size=22).shift(3*RIGHT+2.5*UP)
        resposta2=Text("Simétrica em relação ao eixo y ",font_size=22).shift(3*RIGHT+2*UP)
        resposta3=MathTex("cos(-x)=cos(x)",font_size=26).shift(3*RIGHT+1.5*UP)
        cosseno=MathTex("f(x)=cos(x)",font_size=28,color=RED).shift(2.5*UP+2.5*LEFT).set_height(0.5)
        
        
        self.play(Create(axes),Write(axis_labels),run_time=2)
        self.play(Create(simetria))
        self.wait()
        self.play(Write(cosseno))
        self.play(Create(graph),run_time=2)
       
        self.wait(3)
        self.play(FadeOut(graph))
        self.play(Create(graph1),Create(graph2),run_time=5)
    

   
        self.play(Create(resposta))
        self.play(Create(resposta2))
        self.play(Create(resposta3))
        self.wait(4)