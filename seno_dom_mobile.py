from manim import *
from numpy import *

SCALE_FACTOR=0.5
tmp_pixel_height=config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height

config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height *9/16

FRAME_HEIGHT=config.frame_height
FRAME_WIDTH=config.frame_width

EIXO=BLUE

GRAFICO=RED
#     Principais cores:
# - #61acc9 - azul
# - #fd5151 vermelho
# - #fffdec fundo(branco?)

# Cores secundárias:
# - #004aad
# - #d21616
# - #ffffff
# - #000000

class DomSenoMobile(Scene):  
     
     def setup(self, add_border=True):
        if add_border:
            self.border=Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=WHITE
            )
     def construct(self):
        self.camera.background_color= '#fffdec'
         #COORDENADAS
        axes = Axes(x_range=[-10,10],x_length=7,y_range=[-3,3], y_length=5,axis_config={"color": EIXO})
                
       
        point1 = Dot(axes.c2p(0,1), color=RED)
        point2 = Dot(axes.c2p(0,-1), color=RED)
        dominio= Line(axes.c2p(-10,0), axes.c2p(10,0),stroke_width = 6, stroke_color = GRAFICO)
        imagem=Line(axes.c2p(0,-1), axes.c2p(0,1),stroke_width = 6, stroke_color = GRAFICO )
        graph = axes.plot((lambda x: sin(x)), x_range=[-10, 10], color=GRAFICO)
        graph2 = axes.plot((lambda x: sin(x)), x_range=[-10, 10], color=GRAFICO)

        #TEXTOS
        mathtext1= MathTex("f(x)=sen(x)").set_color_by_gradient(GRAFICO).set_height(0.5)
        domtext= MathTex("Dom: \mathbb{R}",color=BLUE)
        imgtext= MathTex("Im: [-1,1]",color=BLUE)
        label1 = MathTex("(0, 1)", color=BLUE, font_size=32).next_to(point1, UP + RIGHT, buff=0.2)
        label2 = MathTex("(0, -1)", color=BLUE, font_size=32).next_to(point2, DOWN + RIGHT, buff=0.2)
        axis_labels=axes.get_axis_labels(x_label="x",y_label="y")
        
        self.play(DrawBorderThenFill(axes))
        self.play(Write(axis_labels))
       
        self.play(mathtext1.animate.shift(UP*2+RIGHT*2.5),run_time=1)
        self.play(Create(graph), run_time=2)
        
        
        self.play(Transform(graph, dominio),run_time=3)
        self.play(domtext.animate.shift(UP*2+LEFT*2),run_time=1)
        self.wait()
        self.play(FadeOut(domtext))
        self.play(FadeOut(graph))

        self.play(Create(graph2), run_time=2)
        self.play(Transform(graph2, imagem),run_time=3)
       
        
        self.play(FadeIn(point1), FadeIn(label1),FadeIn(point2), FadeIn(label2))
        self.wait(2)
        self.play(imgtext.animate.shift(UP*1.98+LEFT*2.75),run_time=1)
        self.wait(4)
     